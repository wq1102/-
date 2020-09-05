import requests
import json
import datetime

class Wechat():
    def __init__(self, openid, name , level):
        self.openid = openid
        self.name = name
        self.level = level
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
        message = "来自"+ self.name + "的" + self.level
        data = {
            "touser": self.openid,
            "template_id": "RbXCxXO68hjr4nvR7ZWNNST1RJxkq3X-flAp8zaFZIc",  # 模板ID
            "url": "https://airkiss-1300565484.cos.ap-nanjing.myqcloud.com/Airkiss/warning.html",  # 点击详情的跳转页面
            "data": {
                "keyword": {
                    "value": message,
                    "color": "#173177"}
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