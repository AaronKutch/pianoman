from music_ir import midi_parse

actionlist = midi_parse("music_ir/example_midis/mary.mid")

f = open('./music_ir/ir_csv/mary.csv', 'w+')
f.write("is_press,time,midi_num\n")
for action in actionlist[1:50]:
    action.modulo_clamp_to_octave(4)
    f.write(f"{action.is_press},{action.time},{action.midi_num}\n")
f.close()
