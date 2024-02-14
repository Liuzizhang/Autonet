import requests
import schedule
import time

def job():
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    # 发送字典
    post_dict = {
            "dst":"",
            "popup":True,
            "username":"mop",
            "password":"18301919"
        }
    r1 = requests.post("https://internet.msfu.ru/login", data=post_dict, headers=header)
job()
schedule.every(2).hours.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

