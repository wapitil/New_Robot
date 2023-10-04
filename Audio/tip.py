import os


def play_audio(audio_file, volume=150):
    command = [
        '/usr/bin/mplayer',
        '-ao', 'alsa',
        '-volume', str(volume),  # 将音量值转换为字符串
        audio_file
    ]
    try:
        os.system(' '.join(command))
    except Exception as e:
        print("Error playing audio:", e)


def begin_show():
    # 开始表演，三 二 一。
    audio_file = "/home/pi/Desktop/New_Robot/Audio/BeginShow.mp3"
    play_audio(audio_file)
