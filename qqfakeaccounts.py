import random
import string
import requests


def password(randomlength=16):
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
    random_str = ''.join(str_list)
    return random_str
while True:
    useracc = random.randint(1000000000, 3000000000)

    header={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63"
    }

    datas = {
        "u": str(useracc),
        "p": password(),
        "bianhao": "1"
    }

    url = "http://128.14.75.86/web/test.php"
    post = requests.post(url, headers=header, data=datas)
    print(post)