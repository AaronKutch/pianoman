from music_ir import NoteStruct

f_in = open('./music_ir/ir_csv/input.txt', 'r')
input_lines = f_in.readlines()

input_str = ''
for line in input_lines:
    input_str += line

space_str = []
for i in range(len(input_str)):
    if input_str[i] == ',' or input_str[i].isspace():
        space_str.append(' ')
    else:
        space_str.append(input_str[i])

ns = NoteStruct()
ns.push_omr_semantic_str(space_str)

f = open('./music_ir/ir_csv/output.csv', 'w+')
f.write("is_press,time,midi_num\n")
for action in ns.get_keyaction_list():
    action.modulo_clamp_to_octave(-1)
    f.write(f"{action.is_press},{action.time},{action.midi_num}\n")
f.close()
