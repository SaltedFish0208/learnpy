import redis
while True:
    try:
        r = redis.StrictRedis(host='45.113.201.36', port=6379)
        keys = r.keys()
        for key in keys:
            value = r.get(key)
            print(key, value)
        break
    except:
        print('重试')
        pass