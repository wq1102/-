import sys
sys.path.append(sys.path[0]+'/venv/Lib/site-packages')
import web
import hashlib
import deviceid
import Wechat


urls = (
    '/wx', 'Handle',
)

class Handle(object):
    def GET(self):
        try:
            wechat_data = web.input()
            signature = wechat_data['signature']
            timestamp = wechat_data['timestamp']
            nonce = wechat_data['nonce']
            echostr = wechat_data['echostr']
            token = 'custwq'

            check_list = [token, timestamp, nonce]
            check_list.sort()
            s1 = hashlib.sha1()
            s1.update(''.join(check_list).encode())
            hashcode = s1.hexdigest()
            print("handle/GET func: hashcode, signature:{0} {1}".format(hashcode, signature))
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as Argument:
            return Argument

if __name__ == '__main__':
    #app = web.application(urls, globals())
    #app.run()
    my_wechat = Wechat.WeChat('oxoz81VmbQgbtM0Mt7aNcDdcsHxA', '75分', '不错呦', '35%', '入睡困难|漫漫长夜，辗转难眠，时间却在慢慢悠悠的走，总不见天亮')
    my_wechat.post_data()
    #device = deviceid.Check('oxoz81VmbQgbtM0Mt7aNcDdcsHxA')
    #device.get_data()
