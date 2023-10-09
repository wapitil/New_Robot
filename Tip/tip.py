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


def opening():
    '请选择表演模式'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/OpenTip.mp3"
    play_audio(audio_file)

def begin_show():
    '开始表演，三 二 一'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/BeginShow.mp3"
    play_audio(audio_file)

def middle():
    '请 下达指令'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/MiddleTip.mp3"
    play_audio(audio_file)

def ending():
    '表演结束，感谢您的观看。'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/EndTip.mp3"
    play_audio(audio_file)

# 以下为 语音模式所有播报 #
def voice_mode():
    '切换为语音模式。'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/VoiceMode.mp3"
    play_audio(audio_file)

def lift_lefthand():
    '举 左手'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/LiftLeftHand.mp3"
    play_audio(audio_file)

def lift_hands():
    '举 双手'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/LiftHands.mp3"
    play_audio(audio_file)

def forword():
    '前进'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/Forword.mp3"
    play_audio(audio_file)

def backword():
    '后退'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/Backword.mp3"
    play_audio(audio_file)

def move_left():
    '左 移'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/MoveLeft.mp3"
    play_audio(audio_file)

def move_right():
    '右 移。'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/MoveRight.mp3"
    play_audio(audio_file)

def turn_left():
    '向 左转。'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/TurnLeft.mp3"
    play_audio(audio_file)

def turn_right():
    '向 右转。'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/TurnRight.mp3"
    play_audio(audio_file)

def leftfootsupport():
    '左脚撑'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/LeftFootSupport.mp3"
    play_audio(audio_file)

def rightfootsupport():
    '右脚撑'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/RightFootSupport.mp3"
    play_audio(audio_file)

# 以下为 视觉模式提示词 #
def camera_init():
    # 相机初始化完成，开始检测。
    audio_file = "/home/pi/Desktop/New_Robot/Tip/CameraInit.mp3"
    play_audio(audio_file)

def big_font():
    '大字站'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/BigFont.mp3"
    play_audio(audio_file)


def lunge():
    '弓箭步'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/Lunge.mp3"
    play_audio(audio_file)

def handsup_vision():
    '举双手'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/HandsUp_Vision.mp3"
    play_audio(audio_file)

def squat_down():
    '蹲下'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/SquatDown.mp3"
    play_audio(audio_file)

def handsonhips():
    '双手叉腰'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/HandsOnHips.mp3"
    play_audio(audio_file)


def waveonehand():
    '挥手'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/WaveOneHand"
    play_audio(audio_file)


# 以下为舞蹈模式提示词 #

def dance_mode():
    # 切换为舞蹈模式。
    audio_file = "/home/pi/Desktop/New_Robot/Tip/DanceMode.mp3"
    play_audio(audio_file)


def song_tip():
    '请 播放第一首音乐'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/SongTip.mp3"
    play_audio(audio_file)


def music_one():
    '音乐编号一'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/MusicOne.mp3"
    play_audio(audio_file)

def music_two():
    '音乐编号二'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/MusicTwo.mp3"
    play_audio(audio_file)


def music_three():
    '音乐编号三'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/MusicThree.mp3"
    play_audio(audio_file)


def music_four():
    '音乐编号四'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/MusicFour.mp3"
    play_audio(audio_file)


def music_five():
    '音乐编号五'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/MusicFive.mp3"
    play_audio(audio_file)

def music_six():
    '音乐编号六'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/MusicSix.mp3"
    play_audio(audio_file)

def song_success():
    '识别成功，请播放 下一首音乐'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/SongSuccess.mp3"
    play_audio(audio_file)


def song_fail():
    '识别失败，请重新播放音乐'
    audio_file = "/home/pi/Desktop/New_Robot/Tip/SongFail.mp3"
    play_audio(audio_file)




if __name__=="__main__":
    ''
    begin_show()
    middle()
    ## 语音 ##
    lift_lefthand()
    # lift_hands()
    # forword()
    # backword()
    # move_left()
    # move_right()
    # turn_left()
    # turn_right()

    ## 视觉 ##
    # camera_init()
    # lunge()

    ## 舞蹈 ##
    # song_tip()
    # music_one()
    # music_two()
    # music_three()
    # music_four()
    # music_five()
    music_six()