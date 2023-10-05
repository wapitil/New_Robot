import numpy as np


def LoopForA():
    # 接受舵机号和角度范围的输入
    servo_data = []

    while True:
        servo_input = input("请输入舵机号（输入'q'以停止添加舵机）：")
        if servo_input.lower() == 'q':
            break

        try:
            servo_number = int(servo_input)
            start_angle = float(input(f"请输入舵机号 {servo_number} 的开始角度："))
            end_angle = float(input(f"请输入舵机号 {servo_number} 的结束角度："))

            servo_data.append((servo_number, start_angle, end_angle))

        except ValueError:
            print("输入无效，请确保输入的是有效的数字。")

    if not servo_data:
        print("没有输入舵机数据，退出程序。")
        return

    # 找到最小的角度范围
    min_angle_range = min(abs(end_angle - start_angle)
                          for _, start_angle, end_angle in servo_data)

    # 生成整体的循环
    print("生成的循环：")

    # 根据舵机数量生成循环变量
    loop_vars = ", ".join([f"var{i}" for i in range(len(servo_data))])

    # 生成大循环
    loop_str = f"for {loop_vars} in zip({', '.join([f'np.arange({start}, {end}, {(end - start) / min_angle_range})' for _, start, end in servo_data])}):"
    print(loop_str)

    # 生成舵机设置操作
    for i, (servo_number, _, _) in enumerate(servo_data):
        print(f"    pwm1.setServoAngleP1({servo_number}, var{i})")


def LoopForB():
    # 接受舵机号和角度范围的输入
    servo_data = []

    while True:
        servo_input = input("请输入舵机号（输入'q'以停止添加舵机）：")
        if servo_input.lower() == 'q':
            break

        try:
            servo_number = int(servo_input)
            start_angle = float(input(f"请输入舵机号 {servo_number} 的开始角度："))
            end_angle = float(input(f"请输入舵机号 {servo_number} 的结束角度："))

            servo_data.append((servo_number, start_angle, end_angle))

        except ValueError:
            print("输入无效，请确保输入的是有效的数字。")

    if not servo_data:
        print("没有输入舵机数据，退出程序。")
        return

    # 找到最小的角度范围
    min_angle_range = min(abs(end_angle - start_angle)
                          for _, start_angle, end_angle in servo_data)

    # 生成整体的循环
    print("生成的循环：")

    # 根据舵机数量生成循环变量
    loop_vars = ", ".join([f"var{i}" for i in range(len(servo_data))])

    # 生成大循环
    loop_str = f"for {loop_vars} in zip({', '.join([f'np.arange({start}, {end}, {(end - start) / min_angle_range})' for _, start, end in servo_data])}):"
    print(loop_str)

    # 生成舵机设置操作
    for i, (servo_number, _, _) in enumerate(servo_data):
        print(f"    pwm2.setServoAngleP2({servo_number}, var{i})")

    print(f"    time.sleep(0.04)")


if __name__ == "__main__":
    board=input("请输入舵机板编号（A为A板,B为B板）：")
    if board =="A":
        LoopForA()
    elif board =="B":
        LoopForB()
