import time

restAngle = [85,75,70,80,65,75,90,80,75,70,60,75,60];

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

for i in range(0,len(restAngle)):
    kit.servo[i].angle = restAngle[i];

print("Servos Zeroed.");