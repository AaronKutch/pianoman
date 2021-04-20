import time

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

restAngle = [85,75,70,80,65,75,90,80,75,70,60,75,60];
playAngle = [100,95,90,100,80,90,120,95,125,85,85,90,80];

#Just reset
servoTesting = [];
#Chrmatic Scale
#servoTesting = [0,1,2,3,4,5,6,7,8,9,10,11,12]
#C Scale
#servoTesting = [0,2,4,5,7,9,11,12]

servoTesting = [0,1,2,3,4,5,6,7,8,9,10,11,12];

for i in range(0,12):
    kit.servo[i].angle = restAngle[i];

time.sleep(1)

for i in servoTesting:
    kit.servo[i].angle = playAngle[i];
    time.sleep(0.25)
    kit.servo[i].angle = restAngle[i];
    time.sleep(.25)
 
time.sleep(3)

for i in range(0,12):
    kit.servo[i].angle = restAngle[i];
    
    
print("ServosTested.");