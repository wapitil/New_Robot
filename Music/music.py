import base64
import wave
import http.client
import json
import subprocess
import time


def record_music(filename, duration):
    command = [
        'sox', '-d', '-c', '1', '-r', '44100', '-b', '16', filename, 'trim', '0', str(
            duration)
    ]
    try:
        subprocess.run(command, check=True)
        print("* done recording")
    except subprocess.CalledProcessError:
        print("Error recording audio")


def wav_to_raw(input_wav_file, output_raw_file):
    with wave.open(input_wav_file, 'rb') as wav_file:
        n_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        frame_rate = wav_file.getframerate()
        frames = wav_file.readframes(wav_file.getnframes())

    with open(output_raw_file, 'wb') as raw_file:
        raw_file.write(frames)


def convert_to_base64(input_raw_file):
    with open(input_raw_file, "rb") as f:
        byte_array = f.read()

    base64_str = base64.b64encode(byte_array).decode("utf-8")

    return base64_str


def music_recognition():
    try:
        wav_to_raw("/home/pi/Desktop/New_Robot/input.wav",
                   r"/home/pi/Desktop/New_Robot/output.raw")
        conn = http.client.HTTPSConnection("shazam.p.rapidapi.com")

        headers = {
            'content-type': "text/plain",
            'X-RapidAPI-Key': "8f0f9d8edamsh2325f4d858ffb8ap1a0b33jsn8355acb7be88",
            'X-RapidAPI-Host': "shazam.p.rapidapi.com"
        }

        payload = convert_to_base64(r"/home/pi/Desktop/New_Robot/output.raw")
        conn.request("POST", "/songs/detect", payload, headers)

        res = conn.getresponse()
        data = res.read()
        parsed_data = json.loads(data)
        print(parsed_data)
        title = parsed_data['track']['title']
        return title
    except KeyError as e:
        print("KeyError:", e)
        return None


def music_main():
    record_music('/home/pi/Desktop/New_Robot/input.wav', 8)
    title = music_recognition()
    return title


if __name__ == "__main__":
    time.sleep(3)
    test = music_main()
    print(test)

    # 将生成的 Base64 编码字符串输出到文件
    base64_string = convert_to_base64(r"/home/pi/Desktop/New_Robot/output.raw")
    with open("output_base64.txt", "w") as base64_file:
        base64_file.write(base64_string)
