import requests as r
from urllib.parse import urlencode
cookie_list = [
]
SENDKEY = "fd8364cb8c547a8c011b66d765502be3"
def checkin():
    for cookie in cookie_list:
        resp = r.get("https://www.luogu.com.cn/index/ajax_punch",cookies = cookie["cookie"],headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4501.0 Safari/537.36 Edg/92.0.891.1"
        }).json()
        msg = "打卡失败\n"
        if resp["code"]==200:
            msg = "打卡成功"
        else:
            msg = msg+resp["message"]
        params = {
            "qq" : cookie["qq"],
            "msg": msg
        }
        url = "https://qmsg.zendee.cn/send/"+SENDKEY+"?"+urlencode(params)
        print(resp)
        resp1 = r.get(url).json()
    return resp1

def main_handler(event, context):
    checkin()


