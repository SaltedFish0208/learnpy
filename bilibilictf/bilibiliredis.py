import redis
while True:
    try:
        #连接redis
        r = redis.StrictRedis(host='45.113.201.36', port=6379)
        keys = r.keys()
        #让我看看你葫芦里装的是什么药
        for key in keys:
            value = r.get(key)
            print(key, value)
        break
    except:
        print('重试')
        pass