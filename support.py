from bs4 import BeautifulSoup
from requests import get
from pymysql import connect


def pourSoup(url, coding='utf-8'):
    '''
        输入url，输出soup
    '''
    try:
        http_response = get(url).content.decode(coding)
    except Exception as e:
        print("Http error: {}".format(e))
    try:
        return BeautifulSoup(http_response, 'html.parser')
    except Exception as e:
        print("BS4 parse error: {}".format(e))

def initial_connection():
    conn = connect(host='localhost',
                   port=3306, user='spider', passwd='spider', db='cellartracker', charset="utf8")
    return conn
    