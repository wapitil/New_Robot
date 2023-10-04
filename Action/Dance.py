import Servo.servo as servo
from Servo.servo_init import setInitialPosition
from Action.Voice import *
import time
import numpy as np
from magnet import *
import threading


def Hats_On():
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)

    for i, j in zip(range(180, 90, -2), range(0, 90, 2)):
        pwm1.setServoAngleP1(3, i)
        pwm1.setServoAngleP1(7, j)
        time.sleep(0.02)

    # 起
    for i, j, k in zip(np.arange(150, 100, -(50/40)), range(200, 120, -2), range(30, 70, 1)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)

    for i in range(90, 180, 5):
        pwm1.setServoAngleP1(5, i)
        time.sleep(0.04)

    for i in range(90, 263, 5):
        pwm1.setServoAngleP1(1, i)
        time.sleep(0.04)
    for i in range(180, 216, 5):
        pwm1.setServoAngleP1(2, i)
        time.sleep(0.04)
    for i in range(90, 170, 5):
        pwm1.setServoAngleP1(4, 170)
        time.sleep(0.04)
    time.sleep(1)

    magnet_thread = threading.Thread(target=Magnet_On, args=(True,))
    magnet_thread.start()
    for i in range(170, 89, -5):
        pwm1.setServoAngleP1(4, i)
        time.sleep(0.04)

    # 那帽子
    for i, j, k, l in zip(np.arange(263, 90, -(263-90)/40), np.arange(90, 180, 90/40), np.arange(90, 150, 60/40), np.arange(216, 190, -26/40)):
        pwm1.setServoAngleP1(1, i)
        pwm1.setServoAngleP1(3, j)
        pwm1.setServoAngleP1(4, k)
        pwm1.setServoAngleP1(2, l)
        time.sleep(0.04)

    # 　蹲下
    for i, j, k in zip(np.arange(105, 150, 1.125), range(120, 200, 2), range(70, 30, -1)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)

    # 鞠躬
    for i, j in zip(range(150, 155, 1), np.arange(180, 225, (225-180)/5)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm1.setServoAngleP1(5, j)
        time.sleep(0.03)

    time.sleep(1)

    for i, j in zip(range(155, 150, -1), np.arange(225, 179, -(225-180)/5)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm1.setServoAngleP1(5, j)
        time.sleep(0.03)

    # 起
    for i, j, k in zip(np.arange(150, 105, -1.125), range(200, 120, -2), range(30, 70, 1)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)

    time.sleep(3)
    stop_magnet_thread = threading.Thread(target=Magnet_On, args=(False,))
    stop_magnet_thread.start()
    # time.sleep(0.5)

    # time.sleep(2)
    # for i in range(90, 175, 5):
    #     pwm1.setServoAngleP1(4, i)
    #     time.sleep(0.04)
    # stop_magnet_thread = threading.Thread(target=Magnet_On, args=(False,))
    # stop_magnet_thread.start()
    # time.sleep(0.5)
    # for i in range(175, 90, -5):
    #     pwm1.setServoAngleP1(4, i)
    #     time.sleep(0.04)
    # for i in range(215, 179, -5):
    #     pwm1.setServoAngleP1(2, i)
    #     time.sleep(0.04)
    # for i in range(260, 90, -5):
    #     pwm1.setServoAngleP1(1, i)
    #     time.sleep(0.04)


def DanceFive_1():
    '下蹲 前举手 上升 收手 两侧展开45'
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

    pwm1.setServoAngleP1(1, 135)
    pwm1.setServoAngleP1(5, 135)
    time.sleep(1)
    pwm1.setServoAngleP1(3, 180)
    pwm1.setServoAngleP1(7, 0)
    time.sleep(1)

    # 　1
    for i, j, k in zip(np.arange(150, 105+(45/3)*2-5, -1.33), np.arange(200, 120+(80/3)*2, -1.77), np.arange(30, 70-(40/3)*2, 0.88)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)

    time.sleep(0.5)

    # 　2
    for i, j, k in zip(np.arange(105+(45/3)*2-5, 105+(45/3)*1-5, -1), np.arange(120+(80/3)*2, 120+(80/3)*1, -1.77), np.arange(70-(40/3)*2, 70-(40/3)*1, 0.88)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)

    time.sleep(0.5)

    # 3
    for i, j, k in zip(np.arange(105+(45/3)*1-5, 105+(45/3)*0, -0.66), np.arange(120+(80/3)*1, 120+(80/3)*0, -1.77), np.arange(70-(40/3)*1, 70-(40/3)*0, 0.88)):
        pwm2.setServoAngleP2(3, i-3)
        pwm2.setServoAngleP2(9, i-3)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.02)
    time.sleep(0.5)

    # 摆手
    for i, j in zip(range(180, 89, -5), range(0, 91, 5)):
        pwm1.setServoAngleP1(3, i)
        pwm1.setServoAngleP1(7, j)
        time.sleep(0.03)
    time.sleep(0.8)
    for i, j in zip(range(135, 89, -5), range(135, 181, 5)):
        pwm1.setServoAngleP1(1, i)
        pwm1.setServoAngleP1(5, j)
        time.sleep(0.03)

    time.sleep(0.8)
    for i, j in zip(range(180, 135, -1), range(0, 45)):
        pwm1.setServoAngleP1(2, i)
        pwm1.setServoAngleP1(6, j)
        time.sleep(0.02)


def DanceFive_2():
    '摆手 下蹲 左移两步 摆手可以改进'
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)

    for i, j in zip(range(90, 135), range(180, 225)):
        pwm1.setServoAngleP1(1, i)
        pwm1.setServoAngleP1(5, j)
        time.sleep(0.01)
    for i, j in zip(range(90, 135), range(90, 135)):
        pwm1.setServoAngleP1(3, i)
        pwm1.setServoAngleP1(7, j)
        time.sleep(0.01)

    for i, j in zip(range(135, 45, -1), range(225, 135, -1)):
        pwm1.setServoAngleP1(1, i)
        pwm1.setServoAngleP1(5, j)
        time.sleep(0.01)
    for i, j in zip(range(135, 45, -1), range(135, 45, -1)):
        pwm1.setServoAngleP1(3, i)
        pwm1.setServoAngleP1(7, j)
        time.sleep(0.01)

    pwm1.setServoAngleP1(1, 90)
    pwm1.setServoAngleP1(5, 180)
    for i in range(45, 90):
        pwm1.setServoAngleP1(3, i)
        pwm1.setServoAngleP1(7, i)
        time.sleep(0.02)
    time.sleep(0.5)
    for i, j in zip(range(90, 150), range(90, 30, -1)):
        pwm1.setServoAngleP1(2, i)
        pwm1.setServoAngleP1(6, j)
        time.sleep(0.02)
    time.sleep(0.5)

    for i, j, k in zip(np.arange(105, 150, 1.125), range(120, 200, 2), range(70, 30, -1)):
        pwm2.setServoAngleP2(3, i)
        pwm2.setServoAngleP2(9, i)
        pwm2.setServoAngleP2(4, j)
        pwm2.setServoAngleP2(10, j)
        pwm2.setServoAngleP2(5, k)
        pwm2.setServoAngleP2(11, k)
        time.sleep(0.01)

    time.sleep(1)
    MoveLeftLoop(2)


def DanceFive_3():
    '向右倾斜 摆手'
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)

    for i, j in zip(np.arange(90, 100, 0.5), range(90, 130, 2)):
        pwm2.setServoAngleP2(2, i)
        pwm2.setServoAngleP2(8, i)
        pwm2.setServoAngleP2(6, i)
        pwm2.setServoAngleP2(12, i)
        pwm1.setServoAngleP1(0, j)
        time.sleep(0.025)

    for i, j in zip(np.arange(150, 120, -(30/20)), range(30, 10, -1)):
        pwm1.setServoAngleP1(2, i)
        pwm1.setServoAngleP1(6, j)
        time.sleep(0.025)

    for i, j in zip(np.arange(100, 80, -1), np.arange(130, 50, -(80/20))):
        pwm2.setServoAngleP2(2, i)
        pwm2.setServoAngleP2(8, i)
        pwm2.setServoAngleP2(6, i)
        pwm2.setServoAngleP2(12, i)
        pwm1.setServoAngleP1(0, j)
        time.sleep(0.04)

    for i, j in zip(range(120, 170, 1), range(10, 60, 1)):
        pwm1.setServoAngleP1(2, i)
        pwm1.setServoAngleP1(6, j)
        time.sleep(0.025)

    for i, j in zip(np.arange(80, 90, 0.5), range(50, 90, 2)):
        pwm2.setServoAngleP2(2, i)
        pwm2.setServoAngleP2(8, i)
        pwm2.setServoAngleP2(6, i)
        pwm2.setServoAngleP2(12, i)
        pwm1.setServoAngleP1(0, j)
        time.sleep(0.025)

    pwm1.setServoAngleP2(2, 150)
    pwm1.setServoAngleP2(6, 30)
    time.sleep(1)


def DanceFive_4():
    '开合手臂 下蹲上来*3 '
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)

    pwm1.setServoAngleP1(2, 180)
    pwm1.setServoAngleP1(6, 0)

    for i, j, k, l in zip(range(90, 180, 1*2), range(180, 90, -1*2), range(90, 180, 1*2), range(90, 0, -1*2)):
        pwm1.setServoAngleP1(1, i)
        pwm1.setServoAngleP1(5, j)
        pwm1.setServoAngleP1(3, k)
        pwm1.setServoAngleP1(7, l)
        time.sleep(0.025)

    for i, j, k in zip(range(180, 90, -1*2), range(0, 90, 1*2), np.arange(90, 30, -(60/90)*2)):
        pwm1.setServoAngleP1(2, i)
        pwm1.setServoAngleP1(6, j)
        pwm1.setServoAngleP1(0, k)
        time.sleep(0.025)

    time.sleep(0.6)

    for i, j, k in zip(range(90, 180, 1*2), range(90, 0, -1*2), np.arange(30, 90,  (60/90)*2)):
        pwm1.setServoAngleP1(2, i)
        pwm1.setServoAngleP1(6, j)
        pwm1.setServoAngleP1(0, k)
        time.sleep(0.025)

    for i, j, k in zip(range(180, 90, -1*2), range(0, 90, 1*2), np.arange(90, 150, (60/90)*2)):
        pwm1.setServoAngleP1(2, i)
        pwm1.setServoAngleP1(6, j)
        pwm1.setServoAngleP1(0, k)
        time.sleep(0.025)

    time.sleep(0.6)

    for i, j, k in zip(range(90, 180, 1*2), range(90, 0, -1*2), np.arange(150, 90, -(60/90)*2)):
        pwm1.setServoAngleP1(2, i)
        pwm1.setServoAngleP1(6, j)
        pwm1.setServoAngleP1(0, k)
        time.sleep(0.025)

    pwm1.setServoAngleP1(4, 150)
    time.sleep(0.5)

    for i, j, k, l in zip(np.arange(150, 30, -(150-30)/90*2), np.arange(180, 150, -30/90*2), range(90, 180, 1*2), range(0, 90,  1*2)):
        pwm1.setServoAngleP1(4, i)
        pwm1.setServoAngleP1(2, j)
        pwm1.setServoAngleP1(5, k)
        pwm1.setServoAngleP1(7, l)
        time.sleep(0.025)

    for i, j, k, l in zip(range(180, 90, -2), range(90, 0, -2), np.arange(30, 90, 60/45), np.arange(0, 30, 30/45)):
        pwm1.setServoAngleP1(5, i)
        pwm1.setServoAngleP1(7, j)
        pwm1.setServoAngleP1(4, k)
        pwm1.setServoAngleP1(6, l)
        time.sleep(0.025)

    time.sleep(1)

    for i in range(3):
        for i, j, k, l, x in zip(np.arange(150, 105+(45/3)*2-5, -1.33), np.arange(200, 120+(80/3)*2, -1.77), np.arange(30, 70-(40/3)*2, 0.88), np.arange(180, 90, -(90/15)), np.arange(0, 90, (90/15))):
            pwm2.setServoAngleP2(3, i)
            pwm2.setServoAngleP2(9, i)
            pwm2.setServoAngleP2(4, j)
            pwm2.setServoAngleP2(10, j)
            pwm2.setServoAngleP2(5, k)
            pwm2.setServoAngleP2(11, k)
            pwm1.setServoAngleP1(3, l)
            pwm1.setServoAngleP1(7, x)
            time.sleep(0.04)

        for i, j, k, l, x in zip(np.arange(105+(45/3)*2-5, 150, 1.33), np.arange(120+(80/3)*2, 200,  1.77), np.arange(70-(40/3)*2, 30,  -0.88), np.arange(90, 180,  (90/15)), np.arange(90, 0, -(90/15))):
            pwm2.setServoAngleP2(3, i)
            pwm2.setServoAngleP2(9, i)
            pwm2.setServoAngleP2(4, j)
            pwm2.setServoAngleP2(10, j)
            pwm2.setServoAngleP2(5, k)
            pwm2.setServoAngleP2(11, k)
            pwm1.setServoAngleP1(3, l)
            pwm1.setServoAngleP1(7, x)
            time.sleep(0.04)

        time.sleep(0.3)


def DanceFour_1():
    '极限下蹲'
    pwm2 = servo.PCA9685(0x41, False)
    pwm2.setPWMFreq(50)
    pwm1 = servo.PCA9685(0x40, False)
    pwm1.setPWMFreq(50)

    # 极限下蹲
    for var0, var1, var2, var3, var4, var5 in zip(np.arange(105, 155, 1), np.arange(105, 155, 1), np.arange(120, 220, (220-120)/45), np.arange(120, 220, (220-120)/45), np.arange(70, 20, -(50/45)), np.arange(70, 20, -(50/45))):
        pwm2.setServoAngleP2(3, var0)
        pwm2.setServoAngleP2(9, var1)
        pwm2.setServoAngleP2(4, var2)
        pwm2.setServoAngleP2(10, var3)
        pwm2.setServoAngleP2(5, var4)
        pwm2.setServoAngleP2(11, var5)
        time.sleep(0.02)

    for i, j, k in zip(np.arange(180, 200, 1), np.arange(90, 180, 90/20), np.arange(90, 150, 60/20)):
        pwm1.setServoAngleP1(2, i)
        pwm1.setServoAngleP1(3, j)
        pwm1.setServoAngleP1(4, k)
        time.sleep(0.02)

    for i, j in zip(np.arange(0, 90, 5), np.arange(90, 151, 60/(90/5))):
        pwm1.setServoAngleP1(6, i)
        pwm1.setServoAngleP1(0, j)
        time.sleep(0.02)

    for i in range(150, 90, -1):
        pwm1.setServoAngleP1(0, i)
        time.sleep(0.02)

    for i, j in zip(range(90, 50, -2), range(80, 100)):
        pwm1.setServoAngleP1(0, i)
        pwm2.setServoAngleP2(1, j)
        pwm2.setServoAngleP2(7, j)
        time.sleep(0.02)

    for i, j in zip(np.arange(50, 130, (130-50)/40), range(100, 60, -1)):
        pwm1.setServoAngleP1(0, i)
        pwm2.setServoAngleP2(1, j)
        pwm2.setServoAngleP2(7, j)
        time.sleep(0.02)
