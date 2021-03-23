from music_ir import NoteStruct

ns = NoteStruct()
ns.push_omr_semantic_str("clef-C1 keySignature-EbM timeSignature-2/4 multirest-23 barline rest-quarter rest-eighth note-Bb4_eighth barline note-Bb4_quarter. note-G4_eighth barline note-Eb5_quarter. note-D5_eighth barline note-C5_eighth note-C5_eighth rest-quarter barline")

# if 60 BPM
unit_time_to_real_time = 1.0
for action in ns.get_keyaction_list():
    action.modulo_clamp_to_octave(4)
    print(f'is_press: {action.is_press}, time: {action.time * unit_time_to_real_time}, clamped midi_num: {action.midi_num}')
