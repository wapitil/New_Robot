from Action.Vision import *
from Action.Voice import *
from Action.Dance import *
from Music.music import music_main
from Tip.tip import *
# from Voice.iat_ws_python3 import
from Voice import iat_ws_python3  as iat

def VoiceMode():
    end = []
    voice_mode() # 切换为语音模式
    while True:
        middle() #　请下达指令
        command=iat.main()
        print(command)
        if command == "举左手。":
            lift_lefthand()
            RaiseLeftHand()
            middle()
        elif command == "举双手。":
            lift_hands()
            # 没写
            middle()
        elif command == "左移。"or command=="左一":
            move_left()
            MoveLeft_Back()
            middle()
        elif command == "右移。"or command == "右一。":
            move_right()
            MoveRight_Back()
            middle()
        elif command == "向左转。":
            turn_left(9)
            TrunLeft_Back()
            middle()
        elif command == "向右转。":
            turn_right()
            TurnRight_Back()
            middle()
        elif command == "左脚撑。":
            # 没写语音提示
            LeftFootSupport()
            middle()
        elif command == "右脚撑。":
            # 没写语音提示
            RightFootSupport()
            middle()
        elif command == "前进。":
            forword()
            GoForward_Back()
            middle()
        elif command == "后退。":
            backword()
            Back_Back()
            middle()
        elif command == "自选动作":
            ''
        elif command == "结束表演。":
            ending()
            break
        else:
            middle()

    pass


def VisionMode():
    flag = [False, False, False, False, False, False]  # 初始状态都设置为 False
    end = []

    while True:

        if len(end) == 4:  # 根据end列表长度判断是否执行过四次动作
            # v.destroy_vision_cap()
            print("执行完毕")
            break


def DanceMode():
    end = []
    song_tip()
    while True:
        # print(f"end={len(end)}") #　检验有几首歌播放了
        music = music_main()  # 调用music_recognition函数，获取音乐识别结果
        # music = input() # 无音乐自测
        print(music)
        if music == "Cheap Thrills":
            '第一首音乐'
            music_one() 

            begin_show()
            DanceRequired()
            end.append(1)
            song_success()
        elif music == "Visions":
            '第二首音乐'
            music_two()

            begin_show()
            DanceRequired()
            end.append(1)
            song_success()
        elif music == "Whatever It Takes":
            '第三首音乐'
            music_three()

            begin_show()
            DanceRequired()
            end.append(1)
            song_success()
        elif music == "Liberators":
            '第四首音乐'
            music_four()

            begin_show()
            DanceRequired()
            end.append(1)
            song_success()
        elif music == "Pacific Rim (feat. Tom Morello)":
            '第五首音乐'
            music_five()

            begin_show()
            DanceRequired()
            end.append(1)
            song_success()
        elif music == "奇迹再现":
            '第六首音乐'
            music_six()

            begin_show()
            DanceOwn()
            end.append(1)
        elif music is None:
            song_fail()
            continue
        if len(end) == 2:  # 根据end列表长度判断是否执行过两次舞蹈

            break


if __name__ == "__main__":
    ''
    while 1:
        opening()
        command=iat.main()
        print(command)
        if command == "视觉模式":
            VisionMode()
            '未决定是否应该通过倒数的方式切换模式'
            DanceMode()
        elif command == "结束表演。":  # 当识别语音为结束时，播报结束提示音并结束整个程序
            ending()
            break
        else:  # 如果识别指令不对，则再次识别
            continue   
            
