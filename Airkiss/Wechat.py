import datetime
import requests
import json
import ast

class WeChat():
    def __init__(self, openid, score, level, power, estimate):
        self.openid = openid
        self.score = score
        self.level = level
        self.data = datetime.datetime.now().strftime('%Y-%m-%d')
        self.power = power
        self.estimate = estimate

    def get_token(self):

        payload = {
                    'grant_type': 'client_credential',
                    'appid': 'wx6a737aa6ea7b4fbb',  # 公众号appid,按自己实际填写
                    'secret': '2ffc719064c6c519c1dddef30fcb1479', #待按自己实际填写
                }
        url = "https://api.weixin.qq.com/cgi-bin/token?"


        respone = requests.get(url, params=payload, timeout=50)
        access_token = respone.json().get("access_token")
        token = "{'access_token':" + str(access_token) + ",'time':" + str(
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + "}"
        # 写入文件
        with open("access_token.txt", "w") as f:
            f.write(token)

        print("get_token", access_token)
        return access_token

    def post_data(self):
        data = {
            "touser": self.openid,
            "template_id": "VX8m7QQnnKipXGd7Gw5GiDSRcYUQpJfZbDPucZdcM64", # 模板ID
            "url": "https://airkiss-1300565484.cos.ap-nanjing.myqcloud.com/Airkiss/index.html", #点击详情的跳转页面
            # "miniprogram":{
            #   "appid":"wx67afc56d7f6cfac0",  #待使用上线小程序appid
            #   "path":"pages/reserve/mgr/mgr"
            # },
            "data":{
                "first": {
                    "value": "您的最新睡眠报告出炉啦！",
                   "color": "#173177"
                },
                "keyword1": {
                    "value": self.data,
                    "color": "#173177"
                },
                "keyword2": {
                    "value": self.score,
                    "color": "#173177"
                },
                "keyword3": {
                    "value": self.level,
                    "color": "#173177"
                },
                "keyword4": {
                    "value": self.power,
                    "color": "#173177"
                },
                "remark": {
                    "value": self.estimate,
                    "color": "#173177"
                }
            }
        }
        json_template = json.dumps(data)
        access_token = self.get_token()
        print("access_token--", access_token)
        url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + access_token
        try:
            respone = requests.post(url, data=json_template, timeout=50)
            # 拿到返回值
            errcode = respone.json().get("errcode")
            print("test--", respone.json())
            if (errcode == 0):
                print("模板消息发送成功")
            else:
                print("模板消息发送失败")
        except Exception as e:
            print("test++", e)


