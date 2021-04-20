# importing csv module
import csv
import threading
import time

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

tempoScale = 2.0
# initializing the titles and rows list

restAngle = [85,75,70,80,65,75,110,80,75,70,60,75,60];
playAngle = [100,95,90,100,80,90,137,95,125,85,85,90,80];

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

def parser():
    global c_list 
    global cs_list
    global d_list 
    global ds_list
    global e_list 
    global f_list 
    global fs_list
    global g_list 
    global gs_list
    global a_list 
    global as_list
    global b_list 
    global c2_list 


    # csv file name
    filename = "music_ir/ir_csv/output.csv"
    rows = []
    
    # reading csv file
    with open(filename, 'r') as csvfile:
        
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

    print(rows)

    for row in rows:
        # parsing each column of a row
        if(row[2]=="0"):
            c_list.append(float(row[1]))

        if(row[2] =="1"):
            cs_list.append(float(row[1]))

        if(row[2] =="2"):
            d_list.append(float(row[1]))

        if(row[2] =="3"):
            ds_list.append(float(row[1]))

        if(row[2] =="4"):
            e_list.append(float(row[1]))

        if(row[2] =="5"):
            f_list.append(float(row[1]))

        if(row[2] =="6"):
            fs_list.append(float(row[1]))

        if(row[2] =="7"):
            g_list.append(float(row[1]))

        if(row[2] =="8"):
            gs_list.append(float(row[1]))

        if(row[2] =="9"):
            a_list.append(float(row[1]))

        if(row[2] =="10"):
            as_list.append(float(row[1]))

        if(row[2] =="11"):
            b_list.append(float(row[1]))

        if(row[2] =="12"):
            c2_list.append(float(row[1]))



    if(len(c_list)%2 == 1):

        c_list.append(c_list[len(c_list)-1]+0.25)


    if(len(cs_list)%2 == 1):

        cs_list.append(cs_list[len(cs_list)-1]+0.25)

    if(len(d_list)%2 == 1):

        d_list.append(d_list[len(d_list)-1]+0.25)


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


    if(len(b_list)%2 == 1):

        b_list.append(b_list[len(b_list)-1]+0.25)


    if(len(c2_list)%2 == 1):

        c2_list.append(c2_list[len(c2_list)-1]+0.25)


            #print(row[1])

def playKey(timeList, servoID):
    print("Here " + str(servoID) + "\n")
    on = False
    previousTime = 0
    for timeStamp in timeList:
        time.sleep((timeStamp - previousTime)*tempoScale)
        if on:
            kit.servo[servoID].angle = restAngle[servoID];
        else:
            kit.servo[servoID].angle = playAngle[servoID];
        on = not on
        previousTime = timeStamp


def main():

    global c_list 
    global cs_list
    global d_list 
    global ds_list
    global e_list 
    global f_list 
    global fs_list
    global g_list 
    global gs_list
    global a_list 
    global as_list
    global b_list 
    global c2_list 

    parser()
    print("in main \n")
    #threading.Thread(target = function, args=(var1, var2, ..., varn,))
    c = threading.Thread(target = playKey, args=(c_list, 0,))
    cs = threading.Thread(target = playKey, args=(cs_list, 1,))
    d = threading.Thread(target = playKey, args=(d_list, 2,))
    ds = threading.Thread(target = playKey, args=(ds_list, 3,))
    e = threading.Thread(target = playKey, args=(e_list, 4,))
    f = threading.Thread(target = playKey, args=(f_list, 5,))
    fs = threading.Thread(target = playKey, args=(fs_list, 6,))
    g = threading.Thread(target = playKey, args=(g_list, 7,))
    gs = threading.Thread(target = playKey, args=(gs_list, 8,))
    a = threading.Thread(target = playKey, args=(a_list, 9,))
    a_s = threading.Thread(target = playKey, args=(as_list, 10,))
    b = threading.Thread(target = playKey, args=(b_list, 11,))
    c2 = threading.Thread(target = playKey, args=(c2_list, 12,))
    
    c.start()
    cs.start()
    d.start()
    ds.start()
    e.start()
    f.start()
    fs.start()
    g.start()
    gs.start()
    a.start()
    a_s.start()
    b.start()
    c2.start()
    
    c.join()
    cs.join()
    d.join()
    ds.join()
    e.join()
    f.join()
    fs.join()
    g.join()
    gs.join()
    a.join()
    a_s.join()
    b.join()
    c2.join()
    #GPIO.cleanup()
    for i in range(0,12):
        kit.servo[i].angle = restAngle[i];
    print("done")
    print(g_list)

#print(g_list,f_list,e_list,d_list,b_list,a_list,c_list)
main()
