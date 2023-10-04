import Servo.servo as servo
from Servo.servo_init import setInitialPosition
import time
import numpy as np


def BigFont():
    '大字站'
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)
    #
    pwm1.setServoAngleP1(2, 90)
    pwm1.setServoAngleP1(6, 90)
    time.sleep(0.5)

    #
    pwm2.setServoAngleP2(6, 105)
    pwm2.setServoAngleP2(12, 75)
    pwm2.setServoAngleP2(2, 105)
    pwm2.setServoAngleP2(8, 75)
    time.sleep(0.5)

    time.sleep(2)

    pwm2.setServoAngleP2(12, 55)
    time.sleep(0.5)
    pwm2.setServoAngleP2(6, 90)
    pwm2.setServoAngleP2(8, 90)
    time.sleep(0.5)
    pwm2.setServoAngleP2(2, 90)
    time.sleep(0.6)
    pwm2.setServoAngleP2(12, 90)

    setInitialPosition()
    pass


def OpenLegs():
    '张腿'
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)
    #
    pwm1.setServoAngleP1(2, 90)
    pwm1.setServoAngleP1(6, 90)
    time.sleep(0.5)

    #
    pwm2.setServoAngleP2(6, 105)
    pwm2.setServoAngleP2(12, 75)
    pwm2.setServoAngleP2(2, 105)
    pwm2.setServoAngleP2(8, 75)
    time.sleep(0.5)


def CloseLegs():
    '合腿'
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)
    pwm2.setServoAngleP2(12, 55)
    time.sleep(0.5)
    pwm2.setServoAngleP2(6, 90)
    pwm2.setServoAngleP2(8, 90)
    time.sleep(0.5)
    pwm2.setServoAngleP2(2, 90)
    time.sleep(0.6)
    pwm2.setServoAngleP2(12, 90)
    setInitialPosition()


def HandsUp():
    '举双手'
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    #
    for i, j in zip(range(90, 271, 5), range(180, 0, -5)):
        pwm1.setServoAngleP1(1, i)
        pwm1.setServoAngleP1(5, j)
        time.sleep(0.04)

    time.sleep(2)

    for i, j in zip(range(271, 89, -2), range(0, 181, 2)):
        pwm1.setServoAngleP1(1, i)
        pwm1.setServoAngleP1(5, j)
        time.sleep(0.02)


def SquatDown():
    '蹲下'
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)

    pwm1.setServoAngleP1(1, 180)
    pwm1.setServoAngleP1(5, 90)

    for i, j, k in zip(range(120, 180, 2), range(105, 135, 1), range(70, 39, -1)):
        pwm2.setServoAngleP2(4, i)
        pwm2.setServoAngleP2(10, i)
        pwm2.setServoAngleP2(3, j)
        pwm2.setServoAngleP2(9, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.005)

    time.sleep(2)

    pwm1.setServoAngleP1(1, 90)
    pwm1.setServoAngleP1(5, 180)

    for i, j, k in zip(range(180, 120, -2), range(135, 105, -1), range(39, 70, 1)):
        pwm2.setServoAngleP2(4, i)
        pwm2.setServoAngleP2(10, i)
        pwm2.setServoAngleP2(3, j)
        pwm2.setServoAngleP2(9, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.01)


def Lunge():
    "弓箭步(右腿前，左手前)"
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)

    pwm2.setServoAngleP2(6, 100)
    pwm2.setServoAngleP2(12, 80)
    pwm2.setServoAngleP2(2, 100)
    pwm2.setServoAngleP2(8, 80)
    time.sleep(1)

    for i, j, k, l, x in zip(np.arange(105, 74, -1.5), np.arange(70, 39, -1.5), np.arange(105, 159, 2.75), np.arange(120, 174, 2.75), np.arange(120, 131, 0.33)):
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(11, j)
        pwm2.setServoAngleP2(3, k)
        pwm2.setServoAngleP2(4, l)
        pwm2.setServoAngleP2(10, x)
        time.sleep(0.04)

    pwm1.setServoAngleP1(5, 45)
    pwm1.setServoAngleP1(1, 45)

    time.sleep(2)
    for i, j in zip(range(45, 181, 3), range(45, 90)):
        pwm1.setServoAngleP1(5, i)
        pwm1.setServoAngleP1(1, j)
        time.sleep(0.04)

    pwm2.setServoAngleP2(9, 105)
    time.sleep(0.1)
    pwm2.setServoAngleP2(11, 70)
    time.sleep(0.1)
    pwm2.setServoAngleP2(3, 105)
    time.sleep(0.1)
    pwm2.setServoAngleP2(4, 120)
    time.sleep(0.1)
    pwm2.setServoAngleP2(10, 120)
    time.sleep(0.1)

    setInitialPosition()
    pass


def HandsOnHips():
    '双手叉腰'
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)

    pwm1.setServoAngleP1(1, 30)
    pwm1.setServoAngleP1(5, 240)
    pwm1.setServoAngleP1(3, 180)
    pwm1.setServoAngleP1(7, 0)

    time.sleep(2)
    setInitialPosition()


def WaveOneHand():
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    for i, j, k in zip(np.arange(180, 90, -1.5), np.arange(90, 180, 1.5), range(90, 150, 1)):
        pwm1.setServoAngleP1(2, i)
        pwm1.setServoAngleP1(1, j)
        pwm1.setServoAngleP1(3, k)
        time.sleep(0.01)
    time.sleep(2)
    for i, j, k in zip(np.arange(90, 180, 1.5), np.arange(180, 90, -1.5), range(150, 90, -1)):
        pwm1.setServoAngleP1(2, i)
        pwm1.setServoAngleP1(1, j)
        pwm1.setServoAngleP1(3, k)
        time.sleep(0.01)
    setInitialPosition()
