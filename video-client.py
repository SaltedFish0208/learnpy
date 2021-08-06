#面向过程

#导入模块
import requests
import json
import time
import os
from clint.textui import progress

#准备
vlc_path = "./vlc-3.0.12"

#正文-说明
print("__      __   _____     _____ _ _             _   ")
time.sleep(0.2)
print(" \ \    / /  |  __ \   / ____| (_)          | |  ")
time.sleep(0.2)
print("  \ \  / /__ | |  | | | |    | |_  ___ _ __ | |_ ")
time.sleep(0.2)
print("   \ \/ / _ \| |  | | | |    | | |/ _ \ '_ \| __|")
time.sleep(0.2)
print("    \  / (_) | |__| | | |____| | |  __/ | | | |_ ")
time.sleep(0.2)
print("     \/ \___/|_____/   \_____|_|_|\___|_| |_|\__|")
time.sleep(0.2)
print("                                          -Powered by Salted_Fish0208")
time.sleep(1)
print("首先，欢迎使用这个软件")
time.sleep(0.2)
print("你可能会问")
time.sleep(0.2)
print("为什么不设计一个ui？")
time.sleep(0.2)
print("既然你诚心诚意的发问了")
time.sleep(0.2)
print("我便大发慈悲的告诉你")
time.sleep(0.2)
print("我懒")
time.sleep(0.2)
print("没错 就只有这么简单\n")
time.sleep(1)
bk1 = input("<按Enter继续>")
#获取视频列表
try:
    url = "http://file.tangmumu.live:10003/videos/22671339/"
    isd = requests.get(url)
    vjson = json.loads(isd.text)
    vlist = []
    print("以下是视频列表")
    print("后缀为-metadata的视频才可以正常拖动进度条")
    print("文件名为.ass的文件是弹幕")
    bk2 = input(("<按Enter继续>"))
    i = 1
    #打印列表
    for elec in vjson:
        print(str(i) + "." + elec['name'])
        vlist.append({str(i):elec['name']})
        i+=1
except :
    print("运行出错了，可能是服务器宕机了，请联系咸鱼咨询详情")
#呼叫vlc
dooronl = input("\n你是想要下载视频还是在线观看\n1-观看\n2-下载\n输入序号：")
if dooronl == "1":
    try:
        chos = input("\n你想观看哪个视频\n在此输入视频序号：")
        net_stream = "http://file.tangmumu.live:10003/videos/22671339/" + vlist[int(chos) - 1][chos]
        os.chdir(vlc_path)
        os.system(f"vlc {net_stream}")
        bk5 = input("<按Enter键退出>")
    except :
        print("运行出错了，可能是你没有将vlc放在同一个目录，或者是视频源有问题，以及输入了空的序号")
        bk3 = input("<按Enter键退出>")
if dooronl == "2":
    dchos = input("\n你想下载哪个视频\n在此输入视频序号：")
    dowreq = url + vlist[int(dchos) - 1][dchos]
    dowl = requests.get(dowreq, stream=True)
    total_length = int(dowl.headers.get('content-length'))
    with open("./download/" + vlist[int(dchos) - 1][dchos], "wb") as f:
        for chunk in progress.bar(dowl.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1, width=100):
            if chunk:
                f.write(chunk)
    bk4 = input("\n下载完成\n<按Enter键退出>")