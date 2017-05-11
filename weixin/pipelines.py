# -*- coding: utf-8 -*-

import pymongo
from bson import ObjectId
from scrapy.exceptions import DropItem

class DropPipeline(object):
    """ 去掉无效的数据
        掉丢不可用数据
        优先级最高
    """
    def  process_item(self, item, spider):
        if not item['account'] and not item['name']:
            raise DropItem('丢掉不可信数据％s：' % item)
        return item


class  MongoPipline():
    """ 存入Mongodb数据库"""
    collection_wechats = 'wechats'
    collection_article = 'article'
    collection_article_data = 'article_data'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'myinfo')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()
        print '本次插数据完成'

    def process_item(self, item, spider):
        try:
            print '准备插入', item['account'],item['name']
            w = self.db[self.collection_wechats].find_one({'account': item['account']})
            if w:   # account exits
                title = self.db[self.collection_article].find_one({'title': item['title']})
                if title: #if cleard url in mongo.if true dorp this item
                    return  item
                _id = self.db[self.collection_wechats].find_one({'account': item['account']})['_id']
                self.db[self.collection_article].insert({'url_o': item['url_o'], 'title': item['title'],
                                                         'author': item['author'],
                                                         'content': item['content'], 'pub_date': item['pub_date'],
                                                         'wechats_id': ObjectId(_id)})
            else:  # account not exist
                _id = self.db[self.collection_wechats].insert({'account': item['account'], 'name': item['name'],
                                                               'description': item['description']})
                self.db[self.collection_article].insert({'url_o': item['url_o'], 'title': item['title'],
                                                         'content': item['content'], 'author': item['author'],
                                                         'pub_date': item['pub_date'], 'wechats_id': ObjectId(_id)})
            print '该条插入完成'
        except Exception,e:
            print '插入mongodb出错',e
        return item







