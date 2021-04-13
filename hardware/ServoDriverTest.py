import time

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

def runServos(arr):
    move = []
    for i, a in enumerate(arr):
        if a == 1:
            move.append(i)
    for a in move:
        kit.servo[a].angle = 180
    time.sleep(0.5)
    for a in move:
        kit.servo[a].angle = 0

try:
    while True:
        runServos([1,0,1,1,0,0,1,0,1,1])
        runServos([0,1,0,1,1,1,0,0,0,0])
        runServos([1,1,0,0,0,1,0,1,1,0])
        runServos([0,1,0,0,0,1,0,0,0,0])
        runServos([1,1,0,1,0,0,0,0,1,0])
        runServos([0,1,1,0,1,0,1,1,1,0])
        runServos([1,1,0,0,0,0,0,0,0,1])
        runServos([0,1,0,0,0,0,0,1,1,0])
        runServos([1,1,1,1,1,0,1,0,1,0])
        runServos([0,1,0,0,0,1,0,0,0,1])
        runServos([1,1,0,0,0,0,0,0,0,0])
        runServos([0,1,1,1,0,0,1,1,0,1])
        runServos([1,1,0,1,1,0,1,0,1,1])
        runServos([0,1,1,0,0,1,0,1,0,0])
        runServos([1,1,0,1,0,0,1,1,1,0])
        
        
        
except KeyboardInterrupt:
    
    
    GPIO.cleanup()
    
print("done")
