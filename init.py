from redis import Redis


def push_redis_list(number, p):
    '''
    向redis增加队列
    '''
    for i in range(number):
        url = "http://www.cellartracker.com/m/wines/{}".format(i)
        p.lpush("wine_info", url)
    p.execute()
    return 0

r = Redis(host='localhost', port=6379, db=0)
p = r.pipeline()
r.delete("wine_info")
push_redis_list(1000000, p)
