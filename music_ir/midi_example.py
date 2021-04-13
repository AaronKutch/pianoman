from music_ir import midi_parse

actionlist = midi_parse("music_ir/example_midis/MarbleMachineRightHand.mid")

for action in actionlist[1:50]:
    action.modulo_clamp_to_octave(4)
    print(f'is_press: {action.is_press}, time: {action.time}, midi_num: {action.midi_num}')
