import midi

import heapq
from enum import Enum

"""
A press (if `self.is_press`) or release (if `!self.is_press`) action on a key specified by `self.midi_num`
"""
class KeyAction:
    def __init__(self, time, is_press, midi_num):
        self.time = time
        self.is_press = is_press
        self.midi_num = midi_num

    def __le__(self, rhs):
        return self.time <= rhs.time

    def __lt__(self, rhs):
        return self.time < rhs.time

    # If `self.midi_num` is outside the specified octave (e.x. Middle C is octave 4), then this will
    # shift the note to be within the specified octave.
    def modulo_clamp_to_octave(self, octave):
        self.midi_num = (self.midi_num % 12) + (octave * 12) + 12

"""
The start time, duration time, and midi number of a note
"""
class Note:
    def __init__(self, start_time, duration, midi_num):
        self.start_time = start_time
        self.duration = duration
        self.midi_num = midi_num

    # Ordered by `self.start_time`, but note that the duration of the note can outlive the starts of
    # other notes
    def __le__(self, rhs):
        return self.start_time <= rhs.start_time

    def __lt__(self, rhs):
        return self.start_time < rhs.start_time

    # Decomposes the note into a press and release `KeyAction`
    def get_actions(self) -> (KeyAction, KeyAction):
        return (
            KeyAction(self.start_time, True, self.midi_num),
            KeyAction(self.start_time + (self.duration * 0.9), False, self.midi_num)
        )

"""
A structure for adding notes for music and creating a queue of press/release actions
"""
class NoteStruct:
    def __init__(self):
        self.notes = []

    def push_note(self, note):
        self.notes.append(note)

    def push_omr_semantic_str(self, semantic_str):
        self.notes.extend(omr_semantic_parse(semantic_str))

    # Get a time ordered sequence of press and release actions
    def get_keyaction_list(self):
        q = []
        for note in self.notes:
            tmp = note.get_actions()
            heapq.heappush(q, tmp[0])
            heapq.heappush(q, tmp[1])
        v = []
        for _ in range(len(q)):
            v.append(heapq.heappop(q))
        return v

# used by the omr parser for note lengths
def figure_multiplier(s):
    # figures
    lut = {
        "quadruple_whole": 4.0,
        "double_whole": 2.0,
        "whole": 1.0,
        "half": 0.5,
        "quarter": 0.25,
        "eighth": 0.125,
        "sixteenth": 0.625,
        "thirty_second": 0.03125,
        "sixty_fourth": 0.015625,
        "hundred_twenty_eighth": 0.0078125,
        "two_hundred_fifty_six": 0.00390625
    }

    last = len(s)

    # ignore any attached `_fermata`, which comes after the dots
    if len(s) >= 8:
        if s[(len(s) - 8):len(s)] == "_fermata":
            last -= 8

    # count the number of dots on the note
    dots = 0
    for i in range(0, last):
        if s[last - i - 1] == '.':
            dots += 1
            last -= 1
        else:
            break

    s2 = s[:last]
    if s2 in lut:
        mul = lut[s2]
        corrected_mul = mul
        for i in range(dots):
            mul /= 2
            corrected_mul += mul
        return corrected_mul
    else:
        return 0.0

# used by the omr parser to convert notes in letter form to midi numbers
def note_handler(t):
    lut = {
        'C': 0,
        'D': 2,
        'E': 4,
        'F': 5,
        'G': 7,
        'A': 9,
        'B': 11,
    }
    i = 0
    # the default values to indicate that note parsing failed
    midi_num = -1
    relative_time = 0
    if t[i] in lut:
        midi_num = lut[t[i]]
        i += 1
        if t[i] == 'b':
            midi_num -= 1
            i += 1
        elif t[i] == '#':
            midi_num += 1
            i += 1
        octave = int(t[i])
        midi_num += ((octave + 1)*12)
        i += 2 # skip the underscore
        relative_time = figure_multiplier(t[i:len(t)])
    return (midi_num, relative_time)

# Parses a string `s` assumed to be in the semantic format from the paper "End-to-End Neural Optical
# Music Recognition of Monophonic Scores". Note that times are normalized so that a quarter note
# takes 1.0 time.
def omr_semantic_parse(input):
    ns = []
    input_i = 0
    current_time = 0
    while True:
        # token
        t = ""
        while input_i < len(input):
            c = input[input_i]
            input_i += 1
            if c == ' ':
                break
            t += c

        midi_num = -1
        relative_time = 0
        gracenote = False
        if (len(t) > 5) and (t[:4] == "rest"):
            relative_time = figure_multiplier(t[5:len(t)])
        elif (len(t) >= 9) and t[:9] == "multirest":
            # TODO fix this to respect time signatures other than 4/4 and to handle the integer
            relative_time = 4.0
        elif (len(t) > 8) and t[:5] == "note-":
            (midi_num, relative_time) = note_handler(t[5:])
        elif (len(t) > 13) and t[:10] == "gracenote-":
            (midi_num, relative_time) = note_handler(t[10:])
            gracenote = True

        if midi_num >= 0 and relative_time > 0:
            # insert a note
            ns.append(Note(current_time, relative_time, midi_num))
            if not gracenote:
                # gracenotes are currently handled by not adding to `current_time`
                current_time += relative_time
        elif relative_time > 0:
            # add to current time
            current_time += relative_time

        if input_i == len(input):
            break
    return ns

"""
Given a path to a `.mid` file, this will return a keyaction list
"""
def midi_parse(path):
    pattern = midi.read_midifile(path)
    beats_per_tick = 1.0 / 1000.0
    actionlist = []
    acc_time = 0
    for track in pattern:
        for event in track:
            if isinstance(event, midi.events.NoteOnEvent):
                t = beats_per_tick * event.tick
                acc_time += t
                action = KeyAction(acc_time, True, event.data[0])
                actionlist.append(action)
            if isinstance(event, midi.events.NoteOffEvent):
                t = beats_per_tick * event.tick
                acc_time += t
                action = KeyAction(acc_time, False, event.data[0])
                actionlist.append(action)
    return actionlist