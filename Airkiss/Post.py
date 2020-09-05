import Warning
import json
data = [{"openid": "oxoz81VmbQgbtM0Mt7aNcDdcsHxA", "name": "张三", "level": "24小时无活动状态警报!"}]
jsondata = json.dumps(data,ensure_ascii=False)
f = open('warning.json', 'w', encoding='utf-8')
f.write(jsondata)
f.close()

with open('warning.json','r',encoding='utf8')as fp:
    message = json.load(fp)
openid = message[0]["openid"]
name = message[0]["name"]
level = message[0]["level"]
my_wechat = Warning.Wechat(openid,name,level)
my_wechat.post_data()