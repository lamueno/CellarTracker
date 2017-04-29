# Welcome

A spider to get wine information on CellarTracker.com

# Plan

## 抓取全部葡萄酒的详细信息
根据实际测试,CellarTracker上目前收录了至少265万种葡萄酒

URL： http://www.cellartracker.com/m/wines/{}
{} 为 从1开始的数字, 最大可以到2650000


## 抓取葡萄酒的社区评论信息
根据葡萄酒详情页的提供的评论数,可以直接获取到该葡萄酒的全部社区评论
``` Python
id = 1
wine_info_soup = pourSoup('http://www.cellartracker.com/m/wines/{}'.format(id))
comment_number = wine_info_soup.find(id='TastingNotes_1').span.string
comment_soup = pourSoup('http://www.cellartracker.com/m/wines/{}/notes?limit={}'.format(id, comment_number))

```

