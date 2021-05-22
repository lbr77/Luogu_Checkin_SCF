import requests as r
from urllib.parse import urlencode
cookie_list = [
    {
        # "cookie": "__client_id=60e12329284353af9eb17348aa13ca22861420c8; _uid=76102",
        "cookie": {
            "__client_id": "",
            "_uid": ""
        },
        "qq": ""
    }
]
SENDKEY = ""
def checkin():
    for cookie in cookie_list:
        resp = r.get("https://www.luogu.com.cn/index/ajax_punch",cookies = cookie["cookie"],headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4501.0 Safari/537.36 Edg/92.0.891.1"
        }).json()
        msg = resp["message"]
        params = {
            "qq" : cookie["qq"],
            "msg": msg
        }
        url = "https://qmsg.zendee.cn/send/"+SENDKEY+"?"+urlencode(params)
        # print(url)
        resp1 = r.get(url).json();
        # print(resp1)

def main_handler():
    checkin()


