import time
import threading


from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

wKAngle = 25;
bKAngle = 25;

ServoAngle = [wKAngle, bKAngle, wKAngle, bKAngle, wKAngle, wKAngle, bKAngle, wKAngle, bKAngle, wKAngle, bKAngle, wKAngle, wKAngle]


#Time List format (start1, stop1, start2, stop2, ..., startn, stopn) In seconds
#Minimum time between stopn-1 and startn is 0.05
c_list  = [1,2,2,2.95,3,4,5,6,7,8]
cs_list = [1,1.95,2,2.95,3,4,5,6,7,8]
d_list  = [4,8]
ds_list = [1,3,5,7]
e_list  = [3,7]
f_list  = [1,2,6,7]
fs_list = [7,8]
g_list  = [8,9]
gs_list = [9,10]
a_list  = [10,11]
as_list = [11,12]
b_list  = [12,13]
c2_list  = [13,14]


def playKey(timeList, servoID):
    print("Here " + str(servoID) + "\n")
    on = False
    previousTime = 0
    for timeStamp in timeList:
        time.sleep(timeStamp - previousTime)
        if on:
            kit.servo[servoID].angle = 0
        else:
            kit.servo[servoID].angle = ServoAngle[servoID]
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

    print("done")
main()