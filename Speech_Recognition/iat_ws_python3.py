# -*- coding:utf-8 -*-
#
#   author: iflytek
#
#  本demo测试时运行的环境为：Windows + Python3.7
#  本demo测试成功运行时所安装的第三方库及其版本如下，您可自行逐一或者复制到一个新的txt文件利用pip一次性安装：
#   cffi==1.12.3
#   gevent==1.4.0
#   greenlet==0.4.15
#   pycparser==2.19
#   six==1.12.0
#   websocket==0.2.1
#   websocket-client==0.56.0
#
#  语音听写流式 WebAPI 接口调用示例 接口文档（必看）：https://doc.xfyun.cn/rest_api/语音听写（流式版）.html
#  webapi 听写服务参考帖子（必看）：http://bbs.xfyun.cn/forum.php?mod=viewthread&tid=38947&extra=
#  语音听写流式WebAPI 服务，热词使用方式：登陆开放平台https://www.xfyun.cn/后，找到控制台--我的应用---语音听写（流式）---服务管理--个性化热词，
#  设置热词
#  注意：热词只能在识别的时候会增加热词的识别权重，需要注意的是增加相应词条的识别率，但并不是绝对的，具体效果以您测试为准。
#  语音听写流式WebAPI 服务，方言试用方法：登陆开放平台https://www.xfyun.cn/后，找到控制台--我的应用---语音听写（流式）---服务管理--识别语种列表
#  可添加语种或方言，添加后会显示该方言的参数值
#  错误码链接：https://www.xfyun.cn/document/error-code （code返回错误码时必看）
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import websocket
import datetime
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

STATUS_FIRST_FRAME = 0  # 第一帧的标识
STATUS_CONTINUE_FRAME = 1  # 中间帧标识
STATUS_LAST_FRAME = 2  # 最后一帧的标识

# 用于存储识别结果的全局变量
recognition_result = None


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
        # print("date: ",date)
        # print("v: ",v)
        # 此处打印出建立连接时候的url,参考本demo的时候可取消上方打印的注释，比对相同参数时生成的url与自己代码生成的url是否一致
        # print('websocket url :', url)
        return url


def recognize_audio():
    wsParam = Ws_Param(APPID='27240ce9', APISecret='NDU1MDU3ZmQwYTZlODdmZDk1NTllZmE0',
                       APIKey='3ea5d9833cc04a566fdf94b403d16cba',
                       AudioFile=r'C:\Users\10426\Desktop\Robot\Speech_Recognition\output.wav')

    def on_message(ws, message):
        # 收到websocket消息的处理

        # 在on_message函数中修改处理方式
        global cached_sentence
        global recognition_result

        try:
            # 将接收到的消息字符串解析为 Python 字典,提取状态码和会话ID
            message_data = json.loads(message)
            code = message_data["code"]
            sid = message_data["sid"]
            # 检查 code 是否为非零值，如果是，则表示识别出现错误。
            if code != 0:
                errMsg = message_data["message"]
                print("sid:%s call error:%s code is:%s" % (sid, errMsg, code))
            else:
                data = message_data["data"]["result"]["ws"]
                current_sn = message_data["data"]["result"]["sn"]  # 标识当前句子的序号
                is_last = message_data["data"]["result"]["ls"]  # 是否是句子的最后一部分

                # 处理识别结果，迭代 data 中的识别结果，将单词或短语连接起来，形成一个完整的句子。
                result = ""
                for i in data:
                    for w in i["cw"]:
                        result += w["w"]

                # 如果是新的句子，将之前缓存的句子加上
                if current_sn == 1:
                    cached_sentence = result
                else:
                    cached_sentence += result

                # 如果是句子的最后一部分，返回完整的句子并清空缓存
                if is_last:
                    complete_sentence = cached_sentence
                    cached_sentence = ""  # 清空缓存
                    # process_recognition_result(
                    #     complete_sentence)  # 调用处理函数处理识别结果
                    recognition_result = complete_sentence
        except Exception as e:
            print("receive msg, but parse exception:", e)

    def on_error(ws, error):
        print("### error:", error)

    def on_close(ws, a, b):
        print("### closed ###")

    def on_open(ws):
        def run(*args):
            frameSize = 8000  # 每一帧的音频大小
            intervel = 0.04  # 发送音频间隔(单位:s)
            status = STATUS_FIRST_FRAME  # 音频的状态信息，标识音频是第一帧，还是中间帧、最后一帧

            with open(wsParam.AudioFile, "rb") as fp:
                while True:
                    buf = fp.read(frameSize)
                    # 文件结束
                    if not buf:
                        status = STATUS_LAST_FRAME
                    # 第一帧处理
                    # 发送第一帧音频，带business 参数
                    # appid 必须带上，只需第一帧发送
                    if status == STATUS_FIRST_FRAME:

                        d = {"common": wsParam.CommonArgs,
                             "business": wsParam.BusinessArgs,
                             "data": {"status": 0, "format": "audio/L16;rate=16000",
                                      "audio": str(base64.b64encode(buf), 'utf-8'),
                                      "encoding": "raw"}}
                        d = json.dumps(d)
                        ws.send(d)
                        status = STATUS_CONTINUE_FRAME
                    # 中间帧处理
                    elif status == STATUS_CONTINUE_FRAME:
                        d = {"data": {"status": 1, "format": "audio/L16;rate=16000",
                                      "audio": str(base64.b64encode(buf), 'utf-8'),
                                      "encoding": "raw"}}
                        ws.send(json.dumps(d))
                    # 最后一帧处理
                    elif status == STATUS_LAST_FRAME:
                        d = {"data": {"status": 2, "format": "audio/L16;rate=16000",
                                      "audio": str(base64.b64encode(buf), 'utf-8'),
                                      "encoding": "raw"}}
                        ws.send(json.dumps(d))
                        time.sleep(1)
                        break
                    # 模拟音频采样间隔
                    time.sleep(intervel)
            ws.close()

        thread.start_new_thread(run, ())

    # 创建WebSocket连接并运行
    wsUrl = wsParam.create_url()
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(
        wsUrl, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    # 返回识别结果或其他需要的信息
    return None


def main():
    recognize_audio()
    return recognition_result


if __name__ == "__main__":
    # 创建WebSocket连接并运行
    time1 = time.time()
    recognize_audio()

    # 在这里可以使用 recognition_result 来获取识别结果
    print("获取识别结果:", recognition_result)
    time2 = time.time()
    print(time2-time1)
