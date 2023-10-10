from Voice import iat_ws_python3 as iat
from Tip.tip import *
from Music.music import music_main
from Action.Dance import *
from Action.Voice import *
from Action.Vision import *
# from Human_Keypoints_Detection import vision


def VoiceMode():
    end = []
    voice_mode()  # 切换为语音模式
    while True:
        middle()  # 　请下达指令
        command = iat.main()
        print(command)
        if command == "举左手。":
            lift_lefthand()
            # RaiseLeftHand()
        elif command == "举双手。":
            lift_hands()
            # HandsUp_Voice()
        elif command == "左移。" or command == "左一":
            move_left()
            # MoveLeft_Back()
        elif command == "右移。" or command == "右一。":
            move_right()
            # MoveRight_Back()
        elif command == "向左转。":
            turn_left()
            # TrunLeft_Back()
        elif command == "向右转。":
            turn_right()
            # TurnRight_Back()
        elif command == "左脚撑。":
            leftfootsupport()
            # LeftFootSupport()
        elif command == "右脚撑。":
            rightfootsupport()
            # RightFootSupport()
        elif command == "前进。":
            forword()
            # GoForward_Back()
        elif command == "后退。":
            backword()
            # Back_Back()
        elif command == "斜展臂。":
            trapeziusarm()
            # TrapeziusArm()
        elif command == "双手前举。":
            handsforward()
            # HandsForward()
        elif command == "摸头。":
            touchhead()
            # TouchHead()
        elif command == "结束表演。":
            ending()
            break

    pass


def VisionMode(v):
    camera_init()
    flag = [False, False, False, False, False, False, False]  # 初始状态都设置为 False
    end = []
    while True:
        detecting()
        num = v.get_results()
        if num == [1] and not flag[1]:
            big_font()
            BigFont()
            flag[1] = True
            end.append(1)
        elif num == [2] and not flag[2]:
            lunge()
            Lunge()
            flag[2] = True
            end.append(1)
        elif num == [3] and not flag[3]:
            handsup_vision()
            HandsUp_Vision()
            flag[3] = True
            end.append(1)
        elif num == [4] and not flag[4]:
            squat_down()
            SquatDown()
            flag[4] = True
            end.append(1)
        elif num == [5] and not flag[5]:
            handsonhips()
            HandsOnHips()
            flag[5] = True
            end.append(1)
        elif num == [5] and not flag[5]:
            waveonehand()
            WaveOneHand()
            flag[6] = True
            end.append(1)
        else:
            continue
        if len(end) == 4:  # 根据end列表长度判断是否执行过四次动作
            # v.destroy_vision_cap()
            print("执行完毕")
            break


def DanceMode():
    end = []
    # setInitialPosition()
    time.sleep(1)
    song_tip()
    while True:
        music = music_main()  # 调用music_recognition函数，获取音乐识别结果
        print(music)
        if music == "Cheap Thrills":
            '第一首音乐'
            music_one()
            begin_show()
            # DanceRequired()
            end.append(1)
            song_success()
        elif music == "Visions":
            '第二首音乐'
            music_two()
            begin_show()
            # DanceRequired()
            end.append(1)
            song_success()
        elif music == "Whatever It Takes":
            '第三首音乐'
            music_three()
            begin_show()
            # DanceRequired()
            end.append(1)
            song_success()
        elif music == "Liberators":
            '第四首音乐'
            music_four()
            begin_show()
            # DanceRequired()
            end.append(1)
            song_success()
        elif music == "Pacific Rim (feat. Tom Morello)":
            '第五首音乐'
            music_five()
            begin_show()
            # DanceRequired()
            end.append(1)
            song_success()
        elif music == "奇迹再现":
            '第六首音乐'
            music_six()
            begin_show()
            # DanceOwn()
            end.append(1)
        elif music is None:
            song_fail()
            continue
        if len(end) == 2:  # 根据end列表长度判断是否执行过两次舞蹈
            break


if __name__ == "__main__":
    ''
    # v = vision()

    while 1:
        opening()
        command = iat.main()
        print(command)
        if command == "视觉模式。":
            # VisionMode(v)
            '未决定是否应该通过倒数的方式切换模式'
        elif command == "语音模式。":
            VoiceMode()
        elif command == "舞蹈模式。":  # 识别会有风险
            DanceMode()
        elif command == "结束表演。":  # 当识别语音为结束时，播报结束提示音并结束整个程序
            ending()
            break
        else:  # 如果识别指令不对，则再次识别
            continue
