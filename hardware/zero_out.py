import time


from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

for i in range(0,15):
    kit.servo[i].angle = 90;
  
while(True):
    kit.servo[6].angle = 180;
    time.sleep(1)
    kit.servo[6].angle = 160;
    time.sleep(1)
    
    
print("Servos Zeroed.");