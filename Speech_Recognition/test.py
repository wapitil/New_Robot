import iat_ws_python3 as iat
import recording as rec

if __name__ == "__main__":
    rec.record_audio(
        r"C:\Users\10426\Desktop\Robot\Speech_Recognition\output.wav", 3)
    text = iat.main()
    print(text)
