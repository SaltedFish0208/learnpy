

#导入模块
import requests
import json
import os
#准备
vlc_path = "./vlc-3.0.12"


url = "http://file.tangmumu.live:10003/SaltedFish0208's_Favorite/"
isd = requests.get(url)
mjson = json.loads(isd.text)
mlist = []
i = 1
#打印列表
for elec in mjson:
    print(str(i) + "." + elec['name'])
    mlist.append({str(i):elec['name']})
    i+=1
chos = input("在此输入序号：\n")
net_stream = "http://file.tangmumu.live:10003/SaltedFish0208's_Favorite/" + mlist[int(chos) - 1][chos]
os.chdir(vlc_path)
os.system(f"vlc {net_stream}")
bk5 = input("<按Enter键退出>")