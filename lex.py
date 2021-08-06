#对付蕾皇必备武器库
import requests
import json
import time
import datetime as dt
#蕾皇你现在的粉丝数是多少？
while True:
    try:
        while True:
            target = "https://api.bilibili.com/x/relation/stat?vmid=777536"
            rqs = requests.get(target)
            ins = json.loads(rqs.text)
            ineed = ins["data"]["follower"]
            dtnow = dt.datetime.now().strftime('%F %T')
            #看你掉粉记录。叔叔我啊，可是真的要下架无职转生了
            with open("D:/python-workspace/lexfannum.txt", 'a', encoding='UTF-8') as f:
                f.write("现在是" + dtnow + " 蕾皇粉丝数：" + str(ineed) + "\n")
            print("现在是" + dtnow + " 蕾皇粉丝数：" + str(ineed) + "\n")
            #战术停火
            time.sleep(5)
    except RuntimeError:
        #叔叔我啊，可是真的要封禁你的挨批了
        with open("D:/python-workspace/lexfannum.txt", 'a', encoding='UTF-8') as f:
            f.write("#掉线\n")
        pass