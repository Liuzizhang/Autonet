import random
import requests
from bs4 import BeautifulSoup
import time
import tkinter as tk  # 导入tkinter模块。为了方便后续讲解，命名为 tk。
import tkinter.messagebox  # 引入弹窗库，防止解释器弹出报错。
import re
import schedule
import urllib3
from datetime import datetime
import os

tk.messagebox.showinfo(title='自动网络连接连接程序',message='已启动程序，自动连接МГТУ校园网，程序后台运行，如需关闭程序请启动任务管理器。本窗口可直接关闭。')  # 消息提醒弹窗，点击确定返回值为 ok
seconds=2*60*60
headers_list = [
    {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666'
    }, {
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320'
    }, {
        'user-agent': 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'
    }, {
        'user-agent': 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'
    }, {
        'user-agent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    }, {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    }
]

def time_to_seconds(time_str):
    # 使用正则表达式匹配小时、分钟和秒
    match = re.match(r'(\d+)h(\d+)m(\d+)s', time_str)
    if match:
        # 如果匹配成功，提取小时、分钟和秒
        hours, minutes, seconds = match.groups()
        
        # 将字符串转换为整数
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds) if seconds else 0  # 如果没有秒，设置为0
        
        # 计算总秒数
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return total_seconds
    # 使用正则表达式匹配小时和秒
    match = re.match(r'(\d+)h(\d+)s', time_str)
    if match:
        # 如果匹配成功，提取小时和秒
        hours,  seconds = match.groups()
        
        # 将字符串转换为整数
        hours = int(hours)
        seconds = int(seconds) if seconds else 0  # 如果没有秒，设置为0
        
        # 计算总秒数
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return total_seconds
    else:
        # 如果没有匹配小时，尝试匹配只有分钟和秒的情况
        match = re.match(r'(\d+)m(\d+)s?', time_str)
        
        if match:
            minutes, seconds = match.groups()
            minutes = int(minutes)
            seconds = int(seconds) if seconds else 0  # 如果没有秒，设置为0
            return minutes * 60 + seconds
        
        # 如果没有匹配小时，尝试匹配只有分钟的情况
        match = re.match(r'(\d+)m?', time_str)
        
        if match:
            minutes = match.group(1)
            minutes = int(minutes)
            return minutes * 60
        
        # 如果没有匹配分钟，尝试匹配只有秒的情况
        match = re.match(r'(\d+)s', time_str)
        
        if match:
            seconds = match.group(1)
            return int(seconds)
        
        # 如果没有匹配，返回None或者抛出异常
        return 0


def postreq():
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
    req_out = requests.get(url="https://internet.msfu.ru/logout")
    print("logout and req")
    r1 = requests.post("https://internet.msfu.ru/login", data=post_dict, headers=header, timeout=30)
def settime():
    try:
        headers = random.choice(headers_list)
        req = requests.get(url="https://internet.msfu.ru/status", headers=headers)
        html = req.text
    except urllib3.exceptions.MaxRetryError as e:
        # 如果请求因为重试次数过多而失败，捕获这个异常
        print(f"MaxRetryError: {e}")
        retry()
    except requests.exceptions.SSLError as e:
        # 如果请求因为SSL错误而失败，捕获这个异常
        print(f"SSLError: {e}")
        retry()
    except requests.exceptions.RequestException as e:
        # 捕获其他可能的请求异常
        print(f"RequestException: {e}")
        retry()
    soup = BeautifulSoup(req.text,features="html.parser")
    htmltitle = soup.find("title").text.strip()
    if htmltitle=="internet hotspot > login":
        postreq()
    if htmltitle=="mikrotik hotspot > status":
        company_items = soup.find_all("td")
        gettime=company_items[5].text.strip()
        lefttime=gettime.split("/")[1].replace(" ", "")
        seconds = time_to_seconds(lefttime)
        print(seconds)
        if seconds<600:
            postreq()
            return seconds
def retry():
    # 获取当前时间
    current_time = datetime.now()

    # 打印当前时间
    print("ERROR时间是:", current_time)
settime()
asktime=random.randint(1, 10)
schedule.every(asktime*60).seconds.do(settime)
schedule.every(seconds).seconds.do(postreq)
while True:
    schedule.run_pending()
    time.sleep(1)
