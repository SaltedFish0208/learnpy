import requests
from bs4 import BeautifulSoup
import time
#域名
url = "http://www.biquge.info/55_55325/"
#请求网页
topic = requests.get(url)
looktopic = BeautifulSoup(topic.text,"lxml")
#css选择器-选择a标签的内容
a=looktopic.select(' a')
numb = 0
for i in a:
    #请求网页body
    fullurl = url + i['href']
    print(i['href'])
    data = requests.get(fullurl,stream=True)#stream=True
    code = data.status_code
    what = i['href'].replace(".html"," ")
    try:
        if int(what) > 7642926:
        #定位正文
            if code == 200:
                time.sleep(5)
                print(data)
                lookdata = BeautifulSoup(data.content,'lxml')
                data2 = lookdata.find('div', id="content")
                title = lookdata.title.string
                #保存到本地
                with open("D:/novel/"+title+".txt", 'w+', encoding='UTF-8') as f:
                    try:
                        f.write(str(data2.text))
                    except IOError:
                        print("保存出错")
                    except :
                        pass
            #跳过请求不到的网页
            else:
                print("什么都没有找到")
                numb = numb + 1
                print(numb)
        else:
            pass
    except :
        pass
input('press<ENTER>')
