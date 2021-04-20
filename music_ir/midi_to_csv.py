from music_ir import midi_parse

actionlist = midi_parse("music_ir/example_midis/mhall.mid")

f = open('./music_ir/ir_csv/output.csv', 'w+')
f.write("is_press,time,midi_num\n")
for action in actionlist:
    action.modulo_clamp_to_octave(-1)
    f.write(f"{action.is_press},{action.time},{action.midi_num}\n")
f.close()
