from music_ir import NoteStruct

input_str = """clef-F4, keySignature-EM, timeSignature-C, rest-quarter, rest-eighth,note-G#3_eighth,
note-E3_eighth, note-E3_eighth, note-D#3_eighth,note-C#3_eighth, barline, note-A3_quarter,
rest-eighth, note-A3_eighth,note-D#3_eighth, note-D#3_eighth, note-E3_eighth, note-F#3_eighth,
barline, note-B#2_eighth, rest-sixteenth, note-B2_sixteenth, note-B2_eighth,note-C#3_eighth,
note-D#3_eighth, note-D#3_eighth, note-G#3_eighth,note-D#3_eighth, barline"""

space_str = []
for i in range(len(input_str)):
    if input_str[i] == ',' or input_str[i].isspace():
        space_str.append(' ')
    else:
        space_str.append(input_str[i])

ns = NoteStruct()
ns.push_omr_semantic_str(space_str)

# if 60 BPM
unit_time_to_real_time = 1.0

for note in ns.notes:
    print(f'start_time: {note.start_time * unit_time_to_real_time}, duration: {note.duration * unit_time_to_real_time}, midi_num: {note.midi_num}')

for action in ns.get_keyaction_list():
    action.modulo_clamp_to_octave(4)
    print(f'is_press: {action.is_press}, time: {action.time * unit_time_to_real_time}, clamped midi_num: {action.midi_num}')
