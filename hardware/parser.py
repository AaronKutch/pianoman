# importing csv module
import csv

# csv file name
filename = "mmrh.csv"

# initializing the titles and rows list
fields = []
rows = []

Clist =[]


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
        .append(row[1])

    case 0:
        .append(row[1])

    case 0:
        .append(row[1])

    case 0:
        .append(row[1])

    case 0:
        .append(row[1])

    case 0:
        .append(row[1])

    case 0:
        .append(row[1])

    case 0:
        .append(row[1])

    case 0:
        .append(row[1])

    case 0:
        .append(row[1])

    case 0:
        .append(row[1])

    case 0:
        .append(row[1])



    }
    print(row[1])


    print('\n')
