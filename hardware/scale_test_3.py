import time
import threading


from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)


restAngle = [85,75,70,80,65,75,90,80,75,70,60,75,60];
playAngle = [100,95,90,100,85,90,110,95,125,85,85,90,80];


#Time List format (start1, stop1, start2, stop2, ..., startn, stopn) In seconds
#Minimum time between stopn-1 and startn is 0.05
c_list  = []
cs_list = []
d_list  = []
ds_list = []
e_list  = []
f_list  = [0]
fs_list = []
g_list  = [0]
gs_list = []
a_list  = []
as_list = []
b_list  = []
c2_list  = []

timeTest = 0.3
for i in range (1,11):
    g_list.append(i*timeTest)
    g_list.append(i*timeTest+0.05)
g_list.append(11*timeTest)
for i in range (1,5):
    f_list.append(i*timeTest)
    f_list.append(i*timeTest+0.05)
f_list.append(5*timeTest)

e_list.append(5*timeTest+0.05)
for i in range (6,11):
    e_list.append(i*timeTest)
    e_list.append(i*timeTest+0.05)
e_list.append(11*timeTest)

d_list.append(11*timeTest+0.05)
for i in range (12,18):
    d_list.append(i*timeTest)
    d_list.append(i*timeTest+0.05)
d_list.append(18*timeTest)

b_list.append(11*timeTest+0.05)
for i in range (12,18):
    if(i != 17):
        b_list.append(i*timeTest)
        b_list.append(i*timeTest+0.05)
    else:
        b_list.append((i-1)*timeTest+0.05)
        b_list.append(i*timeTest)
        a_list.append((i-1)*timeTest+0.05)
        a_list.append(i*timeTest)
b_list.append(18*timeTest)
c_list.append(timeTest*19)
c_list.append(timeTest*20)


def playKey(timeList, servoID):
    print("Here " + str(servoID) + "\n")
    on = False
    previousTime = 0
    for timeStamp in timeList:
        time.sleep(timeStamp - previousTime)
        if on:
            kit.servo[servoID].angle = restAngle[servoID];
        else:
            kit.servo[servoID].angle = playAngle[servoID];
        on = not on
        previousTime = timeStamp


def main():
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
print(g_list,f_list,e_list,d_list,b_list,a_list,c_list)
main()