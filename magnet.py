import RPi.GPIO as GPIO
import time


# 在GPIO设置之前禁用警告
GPIO.setwarnings(False)

# 指定用于控制电磁铁的GPIO引脚
electromagnet_pin = 18  # 根据实际情况选择引脚

frequency = 1000  # PWM频率，可以根据需要进行更改
duty_cycle = 0  # 初始占空比，范围是0到100

# 设置GPIO模式为BCM编码
GPIO.setmode(GPIO.BCM)
# 设置GPIO引脚为输出模式
GPIO.setup(electromagnet_pin, GPIO.OUT)

# 创建PWM对象，设置频率和初始占空比
pwm = GPIO.PWM(electromagnet_pin, frequency)
pwm.start(duty_cycle)


def Magnet_On(flag):
    global magnet_thread_running
    magnet_thread_running = flag

    while magnet_thread_running:
        pwm.ChangeDutyCycle(100)
        time.sleep(2)  # 延迟2秒

    # 在需要结束时停止PWM和清理GPIO
    # pwm.ChangeDutyCycle(0)
    pwm.stop()
    GPIO.cleanup()

