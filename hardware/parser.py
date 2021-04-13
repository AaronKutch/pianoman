# importing csv module
import csv

# csv file name
filename = "mmrh.csv"

# initializing the titles and rows list
fields = []
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

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

for row in rows:
    # parsing each column of a row


    Switch(row[2]){

    case 0:
        c_list.append(row[1])

    case 1:
        cs_list.append(row[1])

    case 2:
        d_list.append(row[1])

    case 3:
        ds_list.append(row[1])

    case 4:
        e_list.append(row[1])

    case 5:
        f_list.append(row[1])

    case 6:
        fs_list.append(row[1])

    case 7:
        g_list.append(row[1])

    case 8:
        gs_list.append(row[1])

    case 9:
        a_list.append(row[1])

    case 10:
        as_list.append(row[1])

    case 11:
        b_list.append(row[1])

    case 12:
        c2_list.append(row[1])
    }
    #print(row[1])
