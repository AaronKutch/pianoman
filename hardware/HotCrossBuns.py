import time

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

restAngle = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
playAngle = [15,20,22,20,20,20,20,20,20,20,20,20,20,20,20,20];

playTime = 0.5;
replayKeyRest = 0.1;
restTime = 0.5;            
for i in range(0,5):
    kit.servo[i].angle = restAngle[i];
    
kit.servo[4].angle = playAngle[4];
time.sleep(playTime);
kit.servo[4].angle = restAngle[4];
kit.servo[2].angle = playAngle[2];
time.sleep(playTime);
kit.servo[2].angle = restAngle[2];
kit.servo[0].angle = playAngle[0];
time.sleep(playTime);
kit.servo[0].angle = restAngle[0];
time.sleep(playTime);

kit.servo[4].angle = playAngle[4];
time.sleep(playTime);
kit.servo[4].angle = restAngle[4];
kit.servo[2].angle = playAngle[2];
time.sleep(playTime);
kit.servo[2].angle = restAngle[2];
kit.servo[0].angle = playAngle[0];
time.sleep(playTime);
kit.servo[0].angle = restAngle[0];
time.sleep(playTime);

kit.servo[0].angle = playAngle[0];
time.sleep(playTime - replayKeyRest);
kit.servo[0].angle = restAngle[0];
time.sleep(replayKeyRest);
kit.servo[0].angle = playAngle[0];
time.sleep(playTime);
kit.servo[0].angle = restAngle[0];

kit.servo[2].angle = playAngle[2];
time.sleep(playTime - replayKeyRest);
kit.servo[2].angle = restAngle[2];
time.sleep(replayKeyRest);
kit.servo[2].angle = playAngle[2];
time.sleep(playTime);
kit.servo[2].angle = restAngle[2];

kit.servo[4].angle = playAngle[4];
time.sleep(playTime);
kit.servo[4].angle = restAngle[4];
kit.servo[2].angle = playAngle[2];
time.sleep(playTime);
kit.servo[2].angle = restAngle[2];
kit.servo[0].angle = playAngle[0];
time.sleep(playTime);
kit.servo[0].angle = restAngle[0];



for i in range(0,5):
    kit.servo[i].angle = restAngle[i];
    
    
print("ServosTested.");