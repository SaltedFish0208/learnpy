import requests
from bs4 import BeautifulSoup
import time

url = "http://www.biquge.info/55_55325/"
topic = requests.get(url)
looktopic = BeautifulSoup(topic.text,"lxml")
a=looktopic.select(' a')
numb = 0
for i in a:
    fullurl = url + i['href']
    print(i['href'])
    data = requests.get(fullurl,stream=True)#stream=True
    code = data.status_code
    what = i['href'].replace(".html"," ")
    try:
        if int(what) > 7642926:
            if code == 200:
                time.sleep(5)
                print(data)
                lookdata = BeautifulSoup(data.content,'lxml')
                data2 = lookdata.find('div', id="content")
                title = lookdata.title.string
                with open("D:/novel/"+title+".txt", 'w+', encoding='UTF-8') as f:
                    try:
                        f.write(str(data2.text))
                    except IOError:
                        print("保存出错")
                    except :
                        pass
            else:
                print("什么都没有找到")
                numb = numb + 1
                print(numb)
        else:
            pass
    except :
        pass
input('press<ENTER>')