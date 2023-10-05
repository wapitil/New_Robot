from Action.Vision import *
from Action.Voice import *
from Music.music import music_main


def VoiceMode():
    end = []
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
    while True:
        # print(f"end={len(end)}") #　检验有几首歌播放了
        # music = music_main()  # 调用music_recognition函数，获取音乐识别结果
        music = input()
        # print(music)
        time.sleep(2)  # 等待2秒，等待识别结果
        if music == "Cheap Thrills":
            '第一首音乐'
            end.append(1)
        elif music == "Visions":
            '第二首音乐'
            end.append(1)
        elif music == "Whatever It Takes":
            '第三首音乐'
            end.append(1)
        elif music == "Liberators":
            '第四首音乐'
            end.append(1)
        elif music == "Pacific Rim (feat. Tom Morello)":
            '第五首音乐'
            end.append(1)
        elif music is None:
            continue
        if len(end) == 2:  # 根据end列表长度判断是否执行过两次舞蹈
            break


if __name__ == "__main__":
    DanceMode()
