# -*- coding:utf-8 -*-
import websocket
import hashlib
import base64
import hmac
import json
from urllib.parse import urlencode
import time
import ssl
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import _thread as thread
import os
# import recording as rec  
from Voice import recording as rec

STATUS_FIRST_FRAME = 0  # 第一帧的标识
STATUS_CONTINUE_FRAME = 1  # 中间帧标识
STATUS_LAST_FRAME = 2  # 最后一帧的标识

# 用于存储识别结果的全局变量
recognition_result = ""
cached_sentence = ""


class Ws_Param(object):
    # 初始化
    def __init__(self, APPID, APIKey, APISecret, AudioFile):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.AudioFile = AudioFile

        # 公共参数(common)
        self.CommonArgs = {"app_id": self.APPID}
        # 业务参数(business)，日常用语,中文,中文普通话,静默3s后引擎认为音频结束
        self.BusinessArgs = {"domain": "iat", "language": "zh_cn",
                             "accent": "mandarin", "vinfo": 0, "vad_eos": 3000}

    # 生成url
    def create_url(self):
        url = 'wss://ws-api.xfyun.cn/v2/iat'
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        # 拼接字符串
        signature_origin = "host: " + "ws-api.xfyun.cn" + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + "/v2/iat " + "HTTP/1.1"
        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()
        signature_sha = base64.b64encode(
            signature_sha).decode(encoding='utf-8')

        authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
            self.APIKey, "hmac-sha256", "host date request-line", signature_sha)
        authorization = base64.b64encode(
            authorization_origin.encode('utf-8')).decode(encoding='utf-8')
        # 将请求的鉴权参数组合为字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": "ws-api.xfyun.cn"
        }
        # 拼接鉴权参数，生成url
        url = url + '?' + urlencode(v)
        return url


def recognize_audio():
    wsParam = Ws_Param(APPID='27240ce9', APISecret='NDU1MDU3ZmQwYTZlODdmZDk1NTllZmE0',
                       APIKey='3ea5d9833cc04a566fdf94b403d16cba',
                       AudioFile=r'/home/pi/Desktop/New_Robot/output.wav')

    def on_message(ws, message):
        # 收到websocket消息的处理
        global cached_sentence
        global recognition_result

        try:
            message_data = json.loads(message)
            code = message_data["code"]
            sid = message_data["sid"]
            if code != 0:
                errMsg = message_data["message"]
                print("sid:%s call error:%s code is:%s" % (sid, errMsg, code))
            else:
                data = message_data["data"]["result"]["ws"]
                current_sn = message_data["data"]["result"]["sn"]
                is_last = message_data["data"]["result"]["ls"]

                result = ""
                for i in data:
                    for w in i["cw"]:
                        result += w["w"]

                if current_sn == 1:
                    cached_sentence = result
                else:
                    cached_sentence += result

                if is_last:
                    complete_sentence = cached_sentence
                    cached_sentence = ""
                    recognition_result = complete_sentence
        except Exception as e:
            print("receive msg, but parse exception:", e)

    def on_error(ws, error):
        print("### error:", error)

    def on_close(ws, a, b):
        print("### closed ###")

    def on_open(ws):
        def run(*args):
            frameSize = 8000
            intervel = 0.04
            status = STATUS_FIRST_FRAME

            with open(wsParam.AudioFile, "rb") as fp:
                while True:
                    buf = fp.read(frameSize)
                    if not buf:
                        status = STATUS_LAST_FRAME

                    if status == STATUS_FIRST_FRAME:
                        d = {"common": wsParam.CommonArgs,
                             "business": wsParam.BusinessArgs,
                             "data": {"status": 0, "format": "audio/L16;rate=16000",
                                      "audio": str(base64.b64encode(buf), 'utf-8'),
                                      "encoding": "raw"}}
                        d = json.dumps(d)
                        ws.send(d)
                        status = STATUS_CONTINUE_FRAME
                    elif status == STATUS_CONTINUE_FRAME:
                        d = {"data": {"status": 1, "format": "audio/L16;rate=16000",
                                      "audio": str(base64.b64encode(buf), 'utf-8'),
                                      "encoding": "raw"}}
                        ws.send(json.dumps(d))
                    elif status == STATUS_LAST_FRAME:
                        d = {"data": {"status": 2, "format": "audio/L16;rate=16000",
                                      "audio": str(base64.b64encode(buf), 'utf-8'),
                                      "encoding": "raw"}}
                        ws.send(json.dumps(d))
                        time.sleep(1)
                        break
                    time.sleep(intervel)
            ws.close()

        thread.start_new_thread(run, ())

    wsUrl = wsParam.create_url()
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(
        wsUrl, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    return recognition_result


def main():
    rec.record_audio(r"/home/pi/Desktop/New_Robot/output.wav", 3)
    text = recognize_audio()
    # print(text)
    return text


if __name__ == "__main__":
    main()
