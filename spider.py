from support import *

class Collector(object):
    def __init__(self):
        self.wine_info = None
        self.comments = None
    
    def save(self):
        '''
            将原始数据保存到数据库
        '''
        pass
    
    def get_wine_info(self, id):
        '''
            获取葡萄酒信息
        '''
        url = "http://www.cellartracker.com/wine.asp?iWine={}".format(id)
        self.wine_info = pourSoup(url)
    
    def get_wine_comments(self, id, comment_number)
        '''
            获取评论信息
        '''
        url = "http://www.cellartracker.com/m/wines/{}/notes?limit={}".format(id, comment_number)
        self.comments = pourSoup(url)
    

class Wine(object):
    def __init__(self, id):
        self.id = id
        self.info_document = {}
        self.comments_document = {}
        self.labels_document = {}
    
    def process_info(self, wine_info_soup):
        wine_brief_info = wine_info_soup.find('div', class_='wine-detail')
        wine_detail_list = [each.contents[1][1:] for each in wine_info_soup.find('ul', class_='twin-set-list').find_all('li')]

        self.wine_document={
            "title": wine_brief_info.find('h1').string,
            "best-drink-dates": wine_brief_info.find('span', class_='drink_dates').a.string,
            "scores": {"CT": wine_info_soup.find('div', class_='scores').a.string[2:]},
            "label-image": wine_info_soup.find_all('div', class_='label-image'),
            "vintage": wine_detail_list[0],
            "type": wine_detail_list[1],
            "producer": wine_detail_list[2],
            "varietal": wine_detail_list[3],
            "designation": wine_detail_list[4],
            "vineyard": wine_detail_list[5],
            "country": wine_detail_list[6],
            "region": wine_detail_list[7],
            "sub-region": wine_detail_list[8],
            "appellation": wine_detail_list[9]
        }
        self.comment_number = wine_info_soup.find(id='TastingNotes_1').span.string
    
    def process_comments(self, comment_soup):
        comment_list =[]
        for each in comment_soup.find_all('li'):
            comment_dic = {}
            comment_dic['user_id'] = each.h3.a['href'].split('/')[-1]
            score = each.h3.find('span', class_='score').string
            if score is not None:
                comment_dic['score'] = score[1:-1].split(' ')[0]
            else:
                comment_dic['score'] = -1
            comment_dic['date'] = each.p.get_text().split(' - ')[0]
            comment_dic['body'] = ("".join(each.p.get_text().split(comment_dic['date'])).replace(' - ', '').strip())
            try:
                comment_dic['votes'] = int(each.find('span', class_='notevote').get_text(strip=True).split(' ')[0])
            except AttributeError:
                comment_dic['votes'] = 0
            comment_list.append(comment_dic)
        
        self.comments_document = {
            "wine_id": id,
            "comments": comment_list 
        }




    
