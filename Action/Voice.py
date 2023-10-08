import Servo.servo as servo
from Servo.servo_init import setInitialPosition
import time
import numpy as np

# 自选语音动作未写,举双手未写
def RaiseLeftHand():
    '举左手'
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    for i, j in zip(range(90, 271, 5), range(180, 0, -5)):
        # pwm1.setServoAngleP1(1,i)
        pwm1.setServoAngleP1(5, j)
        time.sleep(0.04)

    time.sleep(2)

    for i, j in zip(range(271, 89, -2), range(0, 181, 2)):
        # pwm1.setServoAngleP1(1,i)
        pwm1.setServoAngleP1(5, j)
        time.sleep(0.02)

def LeftFootSupport():
    '左脚撑 左脚站立'
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)

    pwm2.setServoAngleP2(6, 110)

    for i, j in zip(range(90, 101, 1), np.arange(90, 100, 1)):
        pwm2.setServoAngleP2(2, i)
        pwm2.setServoAngleP2(8, i)
        pwm2.setServoAngleP2(12, j)
        # pwm2.setServoAngleP2(6, i)
        time.sleep(0.04)

    for i, j, k, l in zip(np.arange(105, 145), range(120, 200, 2), range(70, 30, -1), np.arange(100, 106, 0.15)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(12, l)
        time.sleep(0.02)

    time.sleep(2)

    for i in range(100, 90, -1):
        pwm2.setServoAngleP2(8, i)
        time.sleep(0.02)

    for i, j, k, l in zip(np.arange(145, 105, -1), range(200, 120, -2), range(30, 70, 1), np.arange(106, 90, -0.4)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(12, l)
        time.sleep(0.02)

    pwm2.setServoAngleP2(6, 85)
    pwm2.setServoAngleP2(12, 95)
    time.sleep(0.5)
    pwm2.setServoAngleP2(6, 90)
    pwm2.setServoAngleP2(12, 90)
    setInitialPosition()

def RightFootSupport():
    '右脚撑'
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)

    pwm2.setServoAngleP2(12, 80)

    for i, j in zip(range(90, 79, -1), np.arange(90, 79, -1)):
        pwm2.setServoAngleP2(2, i)
        pwm2.setServoAngleP2(8, i)
        # pwm2.setServoAngleP2(12, i)
        pwm2.setServoAngleP2(6, j)
        time.sleep(0.04)

    for i, j, k, l in zip(np.arange(105, 145), range(120, 200, 2), range(70, 30, -1), np.arange(80, 74, -0.15)):
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(11, k)
        pwm2.setServoAngleP2(6, l)
        time.sleep(0.02)

    time.sleep(2)

    for i in range(80, 90, 1):
        pwm2.setServoAngleP2(2, i)
        time.sleep(0.02)

    for i, j, k, l in zip(np.arange(145, 105, -1), range(200, 120, -2), range(30, 70, 1), np.arange(74, 85, 0.275)):
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(11, k)
        pwm2.setServoAngleP2(6, l)
        time.sleep(0.02)

    pwm2.setServoAngleP2(6, 85)
    for i in range(80, 95):
        pwm2.setServoAngleP2(12, i)
        time.sleep(0.05)
    for i in range(85, 91, 1):
        pwm2.setServoAngleP2(6, i)
        time.sleep(0.05)

    pwm2.setServoAngleP2(12, 90)
    setInitialPosition()

def TurnLeft(num):
    '左转'
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)

    for i, j, k in zip(np.arange(105, 150, 1.125), range(120, 200, 2), range(70, 30, -1)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)

    for i in range(num):
        pwm2.setServoAngleP2(6, 80)
        time.sleep(0.5) # 
        pwm2.setServoAngleP2(12, 80)
        time.sleep(0.8) # 
        pwm2.setServoAngleP2(11, 40)
        for i in range(80, 60, -1):
            pwm2.setServoAngleP2(7, i)
            time.sleep(0.02)
        time.sleep(0.3)
        pwm2.setServoAngleP2(11, 30)

        for i, j, k, l in zip(np.arange(80, 105, 1.25), np.arange(150, 153, 0.15), range(200, 220), np.arange(30, 40, 0.5)):
            pwm2.setServoAngleP2(6, i)
            pwm2.setServoAngleP2(12, i)
            pwm2.setServoAngleP2(3, j)
            pwm2.setServoAngleP2(9, j)
            pwm2.setServoAngleP2(4, k)
            # pwm2.setServoAngleP2(11, l)
            time.sleep(0.03)

        time.sleep(0.8) # 

        for i in range(60, 80, 1):
            pwm2.setServoAngleP2(7, i)
            time.sleep(0.02)
        pwm2.setServoAngleP2(3, 150)
        pwm2.setServoAngleP2(9, 150)
        pwm2.setServoAngleP2(4, 200)
        pwm2.setServoAngleP2(5, 30)
        time.sleep(0.3)
        pwm2.setServoAngleP2(6, 90)
        pwm2.setServoAngleP2(12, 90)
        time.sleep(0.3)

    for i, j, k in zip(np.arange(150, 105, -1.125), range(200, 120, -2), range(30, 70, 1)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)

def TurnRight(num):
    '向右转'
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)

    for i, j, k in zip(np.arange(105, 150, 1.125), range(120, 200, 2), range(70, 30, -1)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)

    for i in range(num):
        pwm2.setServoAngleP2(6, 105)
        time.sleep(0.5)
        pwm2.setServoAngleP2(12, 105)
        time.sleep(0.8) # 
        pwm2.setServoAngleP2(5, 33)
        pwm2.setServoAngleP2(1, 100)
        time.sleep(0.5)
        pwm2.setServoAngleP2(5, 30)

        for i, j, k, l in zip(np.arange(105, 80, -1.25), np.arange(150, 157, 0.35), range(200, 220), np.arange(30, 40, 0.5)):
            pwm2.setServoAngleP2(6, i)
            pwm2.setServoAngleP2(12, i)
            pwm2.setServoAngleP2(3, j)
            pwm2.setServoAngleP2(9, j)
            pwm2.setServoAngleP2(10, k)
            # pwm2.setServoAngleP2(11, l)
            time.sleep(0.02)

        time.sleep(0.8) # 

        for i in range(100, 80, -1):
            pwm2.setServoAngleP2(1, i)
            time.sleep(0.02)
        pwm2.setServoAngleP2(9, 150)
        pwm2.setServoAngleP2(3, 150)
        pwm2.setServoAngleP2(10, 200)
        pwm2.setServoAngleP2(11, 30)
        time.sleep(0.5)
        pwm2.setServoAngleP2(6, 90)
        pwm2.setServoAngleP2(12, 90)
        time.sleep(0.3)

    for i, j, k in zip(np.arange(150, 105, -1.125), range(200, 120, -2), range(30, 70, 1)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)

def TrunLeft_Back():
    '左转然后回位'
    TurnLeft(5)
    time.sleep(2)
    TurnRight(6)

def TurnRight_Back():
    '右转然后回位'
    TurnRight(6)
    time.sleep(2)
    TurnLeft(5)

def MoveLeft(num):
    '左移'
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)

    # 下蹲
    for i, j, k in zip(np.arange(105, 150, 1.125), range(120, 200, 2), range(70, 30, -1)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)

    # 张手
    pwm1.setServoAngleP1(2, 135)
    pwm1.setServoAngleP1(6, 45)
    time.sleep(0.5)

    MoveLeftLoop(num)

    # 起身
    for i, j, k in zip(np.arange(150, 105, -1.125), range(200, 120, -2), range(30, 70, 1)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)

def MoveLeftLoop(num):
    '左移下蹲循环'
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)

    for i in range(num):
        for i in range(90, 75, -1):
            pwm2.setServoAngleP2(6, i)
            pwm2.setServoAngleP2(12, i-2)
            time.sleep(0.08)

        pwm2.setServoAngleP2(12, 75)
        pwm2.setServoAngleP2(3, 155)
        pwm2.setServoAngleP2(1, 83)

        for i, j in zip(range(75, 70, -1), range(90, 70, -4)):
            pwm2.setServoAngleP2(12, i)
            pwm2.setServoAngleP2(8, j)
            time.sleep(0.08)

        pwm2.setServoAngleP2(7, 85)  # 　微调
        pwm2.setServoAngleP2(11, 33)
        pwm2.setServoAngleP2(6, 110)

        for k, l in zip(np.arange(90, 110, 1), np.arange(70, 95, 1.25)):
            pwm2.setServoAngleP2(2, k)
            pwm2.setServoAngleP2(8, l)
            pwm2.setServoAngleP2(12, l)
            time.sleep(0.05)

        pwm2.setServoAngleP2(1, 80)
        pwm2.setServoAngleP2(3, 150)
        pwm2.setServoAngleP2(8, 90)

        for i,j in zip(range(95,90,-1),np.arange(110,100,-10/5)):
            pwm2.setServoAngleP2(8, i)
            pwm2.setServoAngleP2(6, j)
            time.sleep(0.05)

        for i, j in zip(np.arange(100, 95, -0.5), range(110, 90, -2)):
            pwm2.setServoAngleP2(6, i)
            pwm2.setServoAngleP2(2, j)
            time.sleep(0.05)
        pwm2.setServoAngleP2(7, 80)

def MoveRight(num):
    '右移'
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)

    for i, j, k in zip(np.arange(105, 150, 1.125), range(120, 200, 2), range(70, 30, -1)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)

    pwm1.setServoAngleP1(2, 135)
    pwm1.setServoAngleP1(6, 45)
    time.sleep(0.5)

    for i in range(num):
        for i in range(90, 105, 1):
            pwm2.setServoAngleP2(6, i+5)
            pwm2.setServoAngleP2(12, i-5)
            time.sleep(0.08)

        pwm2.setServoAngleP2(6, 105)

        for i, j in zip(range(105, 115, 1), range(90, 110, 2)):
            pwm2.setServoAngleP2(6, i)
            pwm2.setServoAngleP2(2, j)
            time.sleep(0.08)

        pwm2.setServoAngleP2(1, 75)
        pwm2.setServoAngleP2(12, 70)
        pwm2.setServoAngleP2(9, 155) #　
        pwm2.setServoAngleP2(7, 80) 

        for k, l in zip(np.arange(90, 70, -1), np.arange(110, 85, -1.25)):
            pwm2.setServoAngleP2(2, l)
            pwm2.setServoAngleP2(8, k)
            pwm2.setServoAngleP2(6, l)
            time.sleep(0.05)

        pwm2.setServoAngleP2(2, 90)
        pwm2.setServoAngleP2(6, 85)
        pwm2.setServoAngleP2(12, 80)
        pwm2.setServoAngleP2(9, 150) # 解决偏移
        pwm2.setServoAngleP2(7, 80)

        for i, j in zip(np.arange(80, 85, 0.5), range(70, 90, 2)):
            pwm2.setServoAngleP2(12, i)
            pwm2.setServoAngleP2(8, j)
            time.sleep(0.05)
        pwm2.setServoAngleP2(1, 80)

    for i, j, k in zip(np.arange(150, 105, -1.125), range(200, 120, -2), range(30, 70, 1)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)

def MoveLeft_Back():
    '左移然后回位'
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    MoveLeft(6)
    time.sleep(2)
    MoveRight(6)
    pwm1.setServoAngleP1(2, 180)
    pwm1.setServoAngleP1(6, 0)

def MoveRight_Back():
    '右移然后回位'
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    MoveRight(6)
    time.sleep(2)
    MoveLeft(6)
    pwm1.setServoAngleP1(2, 180)
    pwm1.setServoAngleP1(6, 0)

def GoForward(num):
    '前进'
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)

    for i, j, k in zip(np.arange(105, 150, 1.125), range(120, 200, 2), range(70, 30, -1)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)

    for var0, var1 in zip(np.arange(90.0, 105.0, 1.0), np.arange(90.0, 105.0, 1.0)):
        pwm2.setServoAngleP2(6, var0)
        pwm2.setServoAngleP2(12, var1)
        time.sleep(0.04)
    
    for i in range(num):
        for var0, var1, var2, var3 in zip(np.arange(150.0, 160.0, 1.0), np.arange(30.0, 40.0, 1.0), np.arange(150.0, 135.0, -15/10), np.arange(30.0, 20.0, -1.0)):
            pwm2.setServoAngleP2(3, var0)
            pwm2.setServoAngleP2(5, var1)
            pwm2.setServoAngleP2(9, var2)
            pwm2.setServoAngleP2(11, var3)
            # time.sleep(0.04)
            time.sleep(0.02)
        
        for var0, var1 in zip(np.arange(105.0, 75.0, -1.0), np.arange(105.0, 75.0, -1.0)):
            pwm2.setServoAngleP2(6, var0)
            pwm2.setServoAngleP2(12, var1)
            time.sleep(0.04)

        for var0, var1, var2, var3 in zip(np.arange(160.0, 140.0, -1.0), np.arange(40.0, 20.0, -1.0), np.arange(135.0, 160.0, 25/20), np.arange(20.0, 40.0, 1.0)):
            pwm2.setServoAngleP2(3, var0)
            pwm2.setServoAngleP2(5, var1)
            pwm2.setServoAngleP2(9, var2)
            pwm2.setServoAngleP2(11, var3)
            # time.sleep(0.04)
            time.sleep(0.02)
        
        for var0, var1 in zip(np.arange(75.0, 105.0, 1.0), np.arange(75.0, 105.0, 1.0)):
            pwm2.setServoAngleP2(6, var0)
            pwm2.setServoAngleP2(12, var1)
            time.sleep(0.04)
        
        for var0, var1, var2, var3 in zip(np.arange(140.0, 150.0, 1.0), np.arange(20.0, 30.0, 1.0), np.arange(160.0, 150.0, -1), np.arange(40.0, 30.0, -1.0)):
            pwm2.setServoAngleP2(3, var0)
            pwm2.setServoAngleP2(5, var1)
            pwm2.setServoAngleP2(9, var2)
            pwm2.setServoAngleP2(11, var3)
            # time.sleep(0.04)
            time.sleep(0.02)

    for var0, var1 in zip(np.arange(105.0, 90.0, -1.0), np.arange(105.0, 90.0, -1.0)):
            pwm2.setServoAngleP2(6, var0)
            pwm2.setServoAngleP2(12, var1)
            time.sleep(0.04)
        
    # 起身
    for i, j, k in zip(np.arange(150, 105, -1.125), np.arange(200, 122, -1.95), range(30, 70, 1)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)

def Back(num):
    '后退'
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)


    for var0, var1, var2, var3, var4, var5 in zip(np.arange(105, 156, 1), np.arange(105, 156, 1), np.arange(120, 220, (220-120)/51), np.arange(120, 220, (220-120)/51), np.arange(70, 20, -(50/51)), np.arange(70, 20, -(50/51))):
        pwm2.setServoAngleP2(3, var0)
        pwm2.setServoAngleP2(9, var1)
        pwm2.setServoAngleP2(4, var2)
        pwm2.setServoAngleP2(10, var3)
        pwm2.setServoAngleP2(5, var4)
        pwm2.setServoAngleP2(11, var5)
        time.sleep(0.02)
    
    time.sleep(0.5)
    for var0, var1 in zip(np.arange(90.0, 102.0, 1.0), np.arange(90.0, 102.0, 1.0)):
        pwm2.setServoAngleP2(6, var0)
        pwm2.setServoAngleP2(12, var1)
        time.sleep(0.04)

    for i in range(num):
        for var0, var1, var2, var3 in zip(np.arange(156.0, 146.0, -1.0), np.arange(20.0, 10.0, -1.0), np.arange(156.0, 166.0, 1.0), np.arange(20.0, 30.0, 1.0)):
            pwm2.setServoAngleP2(3, var0)
            pwm2.setServoAngleP2(5, var1)
            pwm2.setServoAngleP2(9, var2)
            pwm2.setServoAngleP2(11, var3)
            time.sleep(0.02)
        
        for var0, var1 in zip(np.arange(102.0, 77.0, -1.0), np.arange(102.0, 77.0, -1.0)):
            pwm2.setServoAngleP2(6, var0)
            pwm2.setServoAngleP2(12, var1)
            time.sleep(0.04)
        
        for var0, var1, var2, var3 in zip(np.arange(146.0, 166.0, 1.0), np.arange(10.0, 30.0, 1.0), np.arange(166.0, 146.0, -1.0), np.arange(30.0, 10.0, -1.0)):
            pwm2.setServoAngleP2(3, var0)
            pwm2.setServoAngleP2(5, var1)
            pwm2.setServoAngleP2(9, var2)
            pwm2.setServoAngleP2(11, var3)
            time.sleep(0.02)
        
        for var0, var1 in zip(np.arange(77.0, 100.0, 1.0), np.arange(77.0, 100.0, 1.0)):
            pwm2.setServoAngleP2(6, var0)
            pwm2.setServoAngleP2(12, var1)
            time.sleep(0.04)
        
        for var0, var1, var2, var3 in zip(np.arange(166.0, 156.0, -1.0), np.arange(30.0, 20.0, -1.0), np.arange(146.0, 156.0, 1.0), np.arange(10.0, 20.0, 1.0)):
            pwm2.setServoAngleP2(3, var0)
            pwm2.setServoAngleP2(5, var1)
            pwm2.setServoAngleP2(9, var2)
            pwm2.setServoAngleP2(11, var3)
            time.sleep(0.02)
        
    for var0, var1 in zip(np.arange(100.0, 90.0, -1.0), np.arange(100.0, 90.0, -1.0)):
        pwm2.setServoAngleP2(6, var0)
        pwm2.setServoAngleP2(12, var1)
        time.sleep(0.04)
    
    for var0, var1, var2, var3, var4, var5 in zip(np.arange(156.0, 105.0, -1.02), np.arange(156.0, 105.0, -1.02), np.arange(220.0, 120.0, -2.0), np.arange(220.0, 120.0, -2.0), np.arange(20.0, 70.0, 1.0), np.arange(20.0, 70.0, 1.0)):
        pwm2.setServoAngleP2(3, var0)
        pwm2.setServoAngleP2(9, var1)
        pwm2.setServoAngleP2(4, var2)
        pwm2.setServoAngleP2(10, var3)
        pwm2.setServoAngleP2(5, var4)
        pwm2.setServoAngleP2(11, var5)
        time.sleep(0.02)

    # -------------------------------------------------------------------------- #
    # 下蹲(废弃)
    # for i, j, k in zip(np.arange(105, 150, 1.125), range(120, 200, 2), range(70, 30, -1)):
    #     pwm2.setServoAngleP2(3, i)
    #     pwm2.setServoAngleP2(9, i)
    #     pwm2.setServoAngleP2(4, j)
    #     pwm2.setServoAngleP2(10, j)
    #     pwm2.setServoAngleP2(5, k)
    #     pwm2.setServoAngleP2(11, k)
    #     time.sleep(0.02)
    # pwm2.setServoAngleP2(3, 153)
    # pwm2.setServoAngleP2(9, 153)
    # time.sleep(0.2)
    # for var0, var1 in zip(np.arange(90.0, 115.0, 1.0), np.arange(180.0, 165.0, -1.0)):
    #     pwm1.setServoAngleP1(1, var0)
    #     pwm1.setServoAngleP1(5, var1)
    #     time.sleep(0.02)

    # for var0, var1 in zip(np.arange(90.0, 105.0, 1.0), np.arange(90.0, 105.0, 1)):
    #     pwm2.setServoAngleP2(6, var0)
    #     pwm2.setServoAngleP2(12, var1)
    #     time.sleep(0.04)

    # for i in range(3):
    #     for var0, var1, var2, var3 in zip(np.arange(150.0, 140.0, -1.0), np.arange(30.0, 20.0, -1.0), np.arange(150.0, 160.0, 1.0), np.arange(30.0, 40.0, 1.0)):
    #         pwm2.setServoAngleP2(3, var0)
    #         pwm2.setServoAngleP2(5, var1)
    #         pwm2.setServoAngleP2(9, var2)
    #         pwm2.setServoAngleP2(11, var3)
    #         time.sleep(0.04)
        
    #     for var0, var1 in zip(np.arange(105.0, 75.0, -1.0), np.arange(105.0, 75.0, -1.0)):
    #         pwm2.setServoAngleP2(6, var0)
    #         pwm2.setServoAngleP2(12, var1)
    #         time.sleep(0.04)
        
    #     for var0, var1, var2, var3 in zip(np.arange(140.0, 160.0, 1.0), np.arange(20.0, 40.0, 1.0), np.arange(160.0, 140.0, -1.0), np.arange(40.0, 20.0, -1.0)):
    #         pwm2.setServoAngleP2(3, var0)
    #         pwm2.setServoAngleP2(5, var1)
    #         pwm2.setServoAngleP2(9, var2)
    #         pwm2.setServoAngleP2(11, var3)
    #         time.sleep(0.04)
        
    #     for var0, var1 in zip(np.arange(75.0, 105.0, 1.0), np.arange(75.0, 105.0, 1.0)):
    #         pwm2.setServoAngleP2(6, var0)
    #         pwm2.setServoAngleP2(12, var1)
    #         time.sleep(0.04)
        
    #     for var0, var1, var2, var3 in zip(np.arange(160.0, 150.0, -1.0), np.arange(40.0, 30.0, -1.0), np.arange(140.0, 150.0, 1.0), np.arange(20.0, 30.0, 1.0)):
    #         pwm2.setServoAngleP2(3, var0)
    #         pwm2.setServoAngleP2(5, var1)
    #         pwm2.setServoAngleP2(9, var2)
    #         pwm2.setServoAngleP2(11, var3)
    #         time.sleep(0.04)

    # for var0, var1 in zip(np.arange(105.0, 90.0, -1.0), np.arange(105.0, 90.0, -1.0)):
    #     pwm2.setServoAngleP2(6, var0)
    #     pwm2.setServoAngleP2(12, var1)
    #     time.sleep(0.04)
    
    #  # 起身
    # for i, j, k in zip(np.arange(150, 105, -1.125), range(200, 120, -2), range(30, 70, 1)):
    #     pwm2.setServoAngleP2(3, i)
    #     pwm2.setServoAngleP2(9, i)
    #     pwm2.setServoAngleP2(4, j)
    #     pwm2.setServoAngleP2(10, j)
    #     pwm2.setServoAngleP2(5, k)
    #     pwm2.setServoAngleP2(11, k)
    #     time.sleep(0.02)

def GoForward_Back():
    '前进然后回来'
    GoForward(7)
    time.sleep(2)
    Back(7)

def Back_Back():
    '后退然后回来'
    Back(9)
    time.sleep(2)
    GoForward(6)
    


#--------------------------------------------------------------------------------#
# def Back_1(num):
#     '后退 膝盖反'
#     pwm1 = servo.PCA9685(0x40, False)
#     pwm1.setPWMFreq(50)
#     pwm2 = servo.PCA9685(0x41, False)
#     pwm2.setPWMFreq(50)

   
#     for var0, var1, var2, var3, var4, var5 in zip(np.arange(105.0, 100, -1.0), np.arange(105.0, 100, -1.0), np.arange(120.0, 90.0, -30/5), np.arange(120.0, 90.0, -30/5), np.arange(70.0, 90.0, 20/5), np.arange(70.0, 90.0, 20/5)):
#         pwm2.setServoAngleP2(3, var0)
#         pwm2.setServoAngleP2(9, var1)
#         pwm2.setServoAngleP2(4, var2)
#         pwm2.setServoAngleP2(10, var3)
#         pwm2.setServoAngleP2(5, var4)
#         pwm2.setServoAngleP2(11, var5)
#         time.sleep(0.05)
    
#     for var0, var1, var2, var3, var4, var5 in zip(np.arange(100.0, 70.0, -1.0), np.arange(100.0, 70.0, -1.0), np.arange(90.0, 40.0, -50/30), np.arange(90.0, 40.0, -50/30), np.arange(90.0, 115.0, 25/30), np.arange(90.0, 115.0, 25/30)):
#         pwm2.setServoAngleP2(3, var0)
#         pwm2.setServoAngleP2(9, var1)
#         pwm2.setServoAngleP2(4, var2)
#         pwm2.setServoAngleP2(10, var3)
#         pwm2.setServoAngleP2(5, var4)
#         pwm2.setServoAngleP2(11, var5)
#         time.sleep(0.05)

#     for var0, var1, var2, var3, var4, var5 in zip(np.arange(70.0, 50.0, -1.0), np.arange(70.0, 50.0, -1.0), np.arange(40.0, 0.0, -2.0), np.arange(40.0, 0.0, -2.0), np.arange(115.0, 135.0, 1.0), np.arange(115.0, 135.0, 1.0)):
#         pwm2.setServoAngleP2(3, var0)
#         pwm2.setServoAngleP2(9, var1)
#         pwm2.setServoAngleP2(4, var2)
#         pwm2.setServoAngleP2(10, var3)
#         pwm2.setServoAngleP2(5, var4)
#         pwm2.setServoAngleP2(11, var5)
#         time.sleep(0.05)

#     for var0, var1 in zip(np.arange(90.0, 100.0, 1.0), np.arange(180.0, 170.0, -1.0)):
#         pwm1.setServoAngleP1(1, var0)
#         pwm1.setServoAngleP1(5, var1)
#         time.sleep(0.02)

#     for var0, var1 in zip(np.arange(90.0, 105.0, 1.0), np.arange(90.0, 105.0, 1.0)):
#         pwm2.setServoAngleP2(6, var0)
#         pwm2.setServoAngleP2(12, var1)
#         time.sleep(0.06)
    

    
#     for i in range(num):
#         for var0, var1, var2, var3 in zip(np.arange(50.0, 40.0, -1.0), np.arange(135.0, 125.0, -1.0), np.arange(50.0, 60.0, 1.0), np.arange(135.0, 145.0, 1.0)):
#             pwm2.setServoAngleP2(3, var0)
#             pwm2.setServoAngleP2(5, var1)
#             pwm2.setServoAngleP2(9, var2)
#             pwm2.setServoAngleP2(11, var3)
#             time.sleep(0.04)
        
#         for var0, var1 in zip(np.arange(105.0, 75.0, -1.0), np.arange(105.0, 75.0, -1.0)):
#             pwm2.setServoAngleP2(6, var0)
#             pwm2.setServoAngleP2(12, var1)
#             time.sleep(0.06)
        
#         for var0, var1, var2, var3 in zip(np.arange(40.0, 60.0, 1.0), np.arange(125.0, 145.0, 1.0), np.arange(60.0, 40.0, -1.0), np.arange(145.0, 125.0, -1.0)):
#             pwm2.setServoAngleP2(3, var0)
#             pwm2.setServoAngleP2(5, var1)
#             pwm2.setServoAngleP2(9, var2)
#             pwm2.setServoAngleP2(11, var3)
#             time.sleep(0.04)
        
#         for var0, var1 in zip(np.arange(75.0, 105.0, 1.0), np.arange(75.0, 105.0, 1.0)):
#             pwm2.setServoAngleP2(6, var0)
#             pwm2.setServoAngleP2(12, var1)
#             time.sleep(0.06)
        
#         for var0, var2, var3, var4 in zip(np.arange(60.0, 50.0, -1.0),  np.arange(145.0, 135.0, -1.0), np.arange(40.0, 50.0, 1.0), np.arange(125.0, 135.0, 1.0)):
#             pwm2.setServoAngleP2(3, var0)
#             # pwm2.setServoAngleP2(5, var1)
#             pwm2.setServoAngleP2(5, var2)
#             pwm2.setServoAngleP2(9, var3)
#             pwm2.setServoAngleP2(11, var4)
#             time.sleep(0.04)

        
#     for var0, var1 in zip(np.arange(105.0, 90.0, -1.0), np.arange(105.0, 90.0, -1.0)):
#         pwm2.setServoAngleP2(6, var0)
#         pwm2.setServoAngleP2(12, var1)
#         time.sleep(0.04)

#     for var0, var1, var2, var3, var4, var5 in zip(np.arange(50.0, 70.0, 1.0), np.arange(50.0, 70.0, 1.0), np.arange(0.0, 40.0, 2.0), np.arange(0.0, 40.0, 2.0), np.arange(135.0, 115.0, -1.0), np.arange(135.0, 115.0, -1.0)):
#         pwm2.setServoAngleP2(3, var0)
#         pwm2.setServoAngleP2(9, var1)
#         pwm2.setServoAngleP2(4, var2)
#         pwm2.setServoAngleP2(10, var3)
#         pwm2.setServoAngleP2(5, var4)
#         pwm2.setServoAngleP2(11, var5)
#         time.sleep(0.05)
    
#     # for var0, var1, var2, var3, var4, var5 in zip(np.arange(70.0, 100, 1.0), np.arange(70.0, 100.0, 1.0), np.arange(40.0, 90.0, 50/30), np.arange(40.0, 90.0, 50/30), np.arange(115.0, 90.0, -25/30), np.arange(115.0, 90.0, -25/30)):
#     #     pwm2.setServoAngleP2(3, var0)
#     #     pwm2.setServoAngleP2(9, var1)
#     #     pwm2.setServoAngleP2(4, var2)
#     #     pwm2.setServoAngleP2(10, var3)
#     #     pwm2.setServoAngleP2(5, var4)
#     #     pwm2.setServoAngleP2(11, var5)
#     #     time.sleep(0.05)
    
#     for var0, var1 in zip(np.arange(100.0,90.0,  -1.0), np.arange(170.0,180.0,  1.0)):
#         pwm1.setServoAngleP1(1, var0)
#         pwm1.setServoAngleP1(5, var1)
#         time.sleep(0.02)

#     for var0, var1, var2, var3, var4, var5 in zip(np.arange(100, 105.0, 1.0), np.arange(100, 105.0, 1.0), np.arange(90.0, 122.0, 32/5), np.arange(90.0, 122.0, 32/5), np.arange(90.0, 70.0, -20/5), np.arange(90.0, 70.0, -20/5)):
#         pwm2.setServoAngleP2(3, var0)
#         pwm2.setServoAngleP2(9, var1)
#         pwm2.setServoAngleP2(4, var2)
#         pwm2.setServoAngleP2(10, var3)
#         pwm2.setServoAngleP2(5, var4)
#         pwm2.setServoAngleP2(11, var5)
#         time.sleep(0.05)
    
    # def GoForward():
#     '废弃'
#     pwm1 = servo.PCA9685(0x40, False)
#     pwm1.setPWMFreq(50)
#     pwm2 = servo.PCA9685(0x41, False)
#     pwm2.setPWMFreq(50)

    
#     for i in range():

#         for var0, var1, var2 in zip(np.arange(90.0, 76.0, -1.75), np.arange(90.0, 79.0, -1.375), np.arange(70.0, 68.0, -2.0/8)):
#             pwm2.setServoAngleP2(6, var0)
#             pwm2.setServoAngleP2(12, var1)
#             pwm2.setServoAngleP2(5, var2)
#             time.sleep(0.06)

#         time.sleep(0.5)

#         for var0, var1 in zip(np.arange(105.0, 110.0, 1.0), np.arange(105.0, 110.0, 1.0)):
#             pwm2.setServoAngleP2(3, var0)
#             pwm2.setServoAngleP2(9, var1)
#             time.sleep(0.06)

#         time.sleep(0.5)

#         for var0, var1, var2, var3 in zip(np.arange(70.0, 60.0, -1.0), np.arange(70.0, 83.0, 13/10), np.arange(110, 100, -1.0), np.arange(110, 120, 1.0)):
#             pwm2.setServoAngleP2(5, var0)
#             pwm2.setServoAngleP2(11, var1)
#             pwm2.setServoAngleP2(3, var2)
#             pwm2.setServoAngleP2(9, var3)
#             time.sleep(0.06)

#         time.sleep(0.5)

#         for var0, var1 in zip(np.arange(77.0, 90.0, 1.3), np.arange(80.0, 90.0, 1.0)):
#             pwm2.setServoAngleP2(6, var0)
#             pwm2.setServoAngleP2(12, var1)
#             time.sleep(0.06)

#         time.sleep(0.5)

#         #
#         for var0, var1, var2 in zip(np.arange(90.0, 103.0, 1.0), np.arange(90.0, 103.0, 1.0), np.arange(120, 125.0, 5/13)):
#             pwm2.setServoAngleP2(6, var0)
#             pwm2.setServoAngleP2(12, var1)
#             pwm2.setServoAngleP2(9, var2)
#             time.sleep(0.06)
#         time.sleep(0.5)

#         for var0, var1, var2, var3, var4 in zip(np.arange(60.0, 85, 1.5), np.arange(100, 120.0, 1.0), np.arange(80.0, 60.0, -1.0), np.arange(120, 100, -1.0), np.arange(120, 122, 2.0/20)):
#             pwm2.setServoAngleP2(5, var0)
#             pwm2.setServoAngleP2(3, var1)
#             pwm2.setServoAngleP2(11, var2)
#             pwm2.setServoAngleP2(9, var3)
#             pwm2.setServoAngleP2(10, var4)
#             time.sleep(0.06)

#         for i in range(122, 120, -1):
#             pwm2.setServoAngleP2(10, i)
#             time.sleep(0.02)

#         time.sleep(0.5)

#         for var0, var1, var2 in zip(np.arange(85.0, 80.0, -1.0), np.arange(120.0, 125.0, 1.0), np.arange(100.0, 95.0, -1.0)):
#             pwm2.setServoAngleP2(5, var0)
#             pwm2.setServoAngleP2(3, var1)
#             pwm2.setServoAngleP2(9, var2)
#             time.sleep(0.06)

#         time.sleep(0.5)

#         for var0, var1 in zip(np.arange(105.0, 90.0, -1.0), np.arange(105.0, 90.0, -1.0)):
#             pwm2.setServoAngleP2(6, var0)
#             pwm2.setServoAngleP2(12, var1)
#             time.sleep(0.08)

#         # time.sleep(0.5)

#         for var0, var1, var2 in zip(np.arange(90, 77.0, -(90-77)/10), np.arange(90.0, 80.0, -1.0), np.arange(80, 75.0, -5/10)):
#             pwm2.setServoAngleP2(6, var0)
#             pwm2.setServoAngleP2(12, var1)
#             pwm2.setServoAngleP2(5, var2)
#             time.sleep(0.08)

#         time.sleep(0.5)

#         for var0, var1, var2, var3 in zip(np.arange(75.0, 70.0, -1.0), np.arange(125.0, 105.0, -4.0), np.arange(60.0, 70.0, 2.0), np.arange(95.0, 105.0, 2.0)):
#             pwm2.setServoAngleP2(5, var0)
#             pwm2.setServoAngleP2(3, var1)
#             pwm2.setServoAngleP2(11, var2)
#             pwm2.setServoAngleP2(9, var3)
#             time.sleep(0.06)
#         time.sleep(0.5)

#         for var0, var1 in zip(np.arange(77.0, 90.0, 1.3), np.arange(80.0, 90.0, 1.0)):
#             pwm2.setServoAngleP2(6, var0)
#             pwm2.setServoAngleP2(12, var1)
#             time.sleep(0.06)

#         time.sleep(0.5)


# def Back():
#     '作废'
#     pwm1 = servo.PCA9685(0x40, False)
#     pwm1.setPWMFreq(50)
#     pwm2 = servo.PCA9685(0x41, False)
#     pwm2.setPWMFreq(50)

#     for i in range(3):
#         for var0, var1 in zip(np.arange(122.0, 118.0, -1.0), np.arange(122.0, 118.0, -1.0)):
#             pwm2.setServoAngleP2(4, var0)
#             pwm2.setServoAngleP2(10, var1)
#             time.sleep(0.02)

#         # 1
#         for var0, var1, var2, var3 in zip(np.arange(90.0, 77.0, -2.6), np.arange(124.0, 112.0, -2.4), np.arange(90.0, 80.0, -2.0), np.arange(105.0, 110.0, 1.0)):
#             pwm2.setServoAngleP2(6, var0)
#             # pwm2.setServoAngleP2(4, var1)
#             pwm2.setServoAngleP2(12, var2)
#             pwm2.setServoAngleP2(3, var3)
#             time.sleep(0.08)

#         time.sleep(0.5)

#         for var0, var1, var2, var3, var4 in zip(np.arange(70.0, 75.0, 1.0), np.arange(110.0, 125.0, 3.0), np.arange(70.0, 60.0, -2.0), np.arange(105.0, 100.0, -1.0), np.arange(112.0, 124.0, 2.4)):
#             pwm2.setServoAngleP2(5, var0)
#             pwm2.setServoAngleP2(3, var1)
#             pwm2.setServoAngleP2(11, var2)
#             pwm2.setServoAngleP2(9, var3)
#             # pwm2.setServoAngleP2(4, var4)
#             time.sleep(0.08)

#         # for i in range(112, 124):
#         #     pwm2.setServoAngleP2(4, i)
#         #     time.sleep(0.02)

#         time.sleep(0.5)

#         # 2 步进很大
#         for var0, var1, var2 in zip(np.arange(77.0, 105.0, 2.8), np.arange(80.0, 105.0, 2.5), np.arange(60.0, 70.0, 1.0)):
#             pwm2.setServoAngleP2(6, var0)
#             pwm2.setServoAngleP2(12, var1)
#             pwm2.setServoAngleP2(11, var2)
#             time.sleep(0.12)

#         time.sleep(0.5)

#         for var0, var1, var2, var3 in zip(np.arange(75.0, 70.0, -1.0), np.arange(125.0, 100.0, -5.0), np.arange(70.0, 80.0, 2.0), np.arange(100.0, 120.0, 4.0)):
#             pwm2.setServoAngleP2(5, var0)
#             pwm2.setServoAngleP2(3, var1)
#             pwm2.setServoAngleP2(11, var2)
#             pwm2.setServoAngleP2(9, var3)
#             time.sleep(0.08)

#         time.sleep(0.5)

#         # 3
#         for var0, var1, var2, var3 in zip(np.arange(105.0, 77.0, -5.6), np.arange(105.0, 80.0, -5.0), np.arange(100.0, 105.0, 1.0), np.arange(124.0, 112.0, -2.4)):
#             pwm2.setServoAngleP2(6, var0)
#             pwm2.setServoAngleP2(12, var1)
#             pwm2.setServoAngleP2(3, var2)
#             # pwm2.setServoAngleP2(4, var3)
#             time.sleep(0.12)

#         for var0, var1, var2 in zip(np.arange(80.0, 70.0, -1.0), np.arange(120.0, 105.0, -1.5), np.arange(112.0, 124.0, 1.2)):
#             pwm2.setServoAngleP2(11, var0)
#             pwm2.setServoAngleP2(9, var1)
#             # pwm2.setServoAngleP2(4, var2)
#             time.sleep(0.08)

#         # for i in range(112, 124):
#         #     pwm2.setServoAngleP2(4, i)
#         #     time.sleep(0.02)

#         time.sleep(0.5)
