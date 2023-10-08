from Action.Vision import *
from Action.Voice import *
from Action.Dance import *
from Music.music import music_main
from Tip.tip import *
# from Voice.iat_ws_python3 import


def VoiceMode():
    end = []
    
    while True:
       ''

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
        # print(music)
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
    
    VisionMode()
    DanceMode()
