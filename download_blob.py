import requests
import time
from redis import Redis


def get_wine_info_page(r):
    '''
    从redis读取url
    '''
    while(1):
        try:
            url = r.lpop("wine_info").decode()
            download(url)
            time.sleep(1)
            print("get: {}".format(str(url)))
        except:
            print("请求发送失败,重试")
            time.sleep(10)
            continue
    return 0


def download(url):
    try:
        r = requests.get(url, headers=headers, timeout=50)
        print(r.status_code)
        name = url.split('/')[-1]
        f = open('./wine_info/' + str(name) + '.html', 'w')
        f.write(r.content.decode())
        f.close()
    except Exception as e:
        print("文件保存失败：", e)

if __name__ == '__main__':
    headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    r = Redis(host='localhost', port=6379, db=0)
    get_wine_info_page(r)
