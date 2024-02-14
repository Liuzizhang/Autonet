import requests
from bs4 import BeautifulSoup
import time
import tkinter as tk  # 导入tkinter模块。为了方便后续讲解，命名为 tk。
import tkinter.messagebox  # 引入弹窗库，防止解释器弹出报错。
tk.messagebox.showinfo(title='自动网络连接连接程序',message='已启动程序，自动连接МГТУ校园网，程序后台运行，如需关闭程序请启动任务管理器。本窗口可直接关闭。')  # 消息提醒弹窗，点击确定返回值为 ok

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

while True:
    req = requests.get(url="https://internet.msfu.ru/status")
    html=req.text
    soup = BeautifulSoup(req.text,features="html.parser")
    htmltitle = soup.find("title").text.strip()
    if htmltitle=="internet hotspot > login":
        job()

    if htmltitle=="mikrotik hotspot > status":
        company_items = soup.find_all("td")
        gettime=company_items[5].text.strip()
        lefttime=gettime.split("/")[1]
        if 'h' not in lefttime and 'm' not in lefttime:
            req_out = requests.get(url="https://internet.msfu.ru/logout")
            job()
        if 'h' in lefttime:
            time.sleep(1*60*60)
