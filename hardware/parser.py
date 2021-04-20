# importing csv module
import csv

# csv file name
filename = "music_ir/ir_csv/output.csv"

# initializing the titles and rows list

rows = []

c_list  = []
cs_list = []
d_list  = []
ds_list = []
e_list  = []
f_list  = []
fs_list = []
g_list  = []
gs_list = []
a_list  = []
as_list = []
b_list  = []
c2_list  = []


# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

for row in rows:
    # parsing each column of a row
    if(row[2]==0):
        c_list.append(row[1])

    if(row[2] ==1):
        cs_list.append(row[1])

    if(row[2] ==2):
        d_list.append(row[1])

    if(row[2] ==3):
        ds_list.append(row[1])

    if(row[2] ==4):
        e_list.append(row[1])

    if(row[2] ==5):
        f_list.append(row[1])

    if(row[2] ==6):
        fs_list.append(row[1])

    if(row[2] ==7):
        g_list.append(row[1])

    if(row[2] ==8):
        gs_list.append(row[1])

    if(row[2] ==9):
        a_list.append(row[1])

    if(row[2] ==10):
        as_list.append(row[1])

    if(row[2] ==11):
        b_list.append(row[1])

    if(row[2] ==12):
        c2_list.append(row[1])



if(len(c_list)%2 == 1):

    c_list.append(c_list[len(c_list)-1]+0.25)


if(len(cs_list)%2 == 1):

    cs_list.append(cs_list[len(cs_list)-1]+0.25)

if(len(d_list)%2 == 1):

    d_list.append(d_list[len(c_list)-1]+0.25)


if(len(ds_list)%2 == 1):

    ds_list.append(ds_list[len(ds_list)-1]+0.25)


if(len(e_list)%2 == 1):

    e_list.append(e_list[len(e_list)-1]+0.25)


if(len(f_list)%2 == 1):

    f_list.append(f_list[len(f_list)-1]+0.25)


if(len(fs_list)%2 == 1):

    fs_list.append(fs_list[len(fs_list)-1]+0.25)


if(len(g_list)%2 == 1):

    g_list.append(g_list[len(g_list)-1]+0.25)


if(len(gs_list)%2 == 1):

    gs_list.append(gs_list[len(gs_list)-1]+0.25)



if(len(a_list)%2 == 1):

    a_list.append(a_list[len(a_list)-1]+0.25)


if(len(as_list)%2 == 1):

    as_list.append(as_list[len(as_list)-1]+0.25)


if(len(c_list)%2 == 1):

    b_list.append(b_list[len(b_list)-1]+0.25)


if(len(c_list)%2 == 1):

    c2_list.append(c2_list[len(c2_list)-1]+0.25)


            #print(row[1])
