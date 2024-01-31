# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import csv
import pymysql
class BookPipeline(object):
    def __init__(self):
        self.f=open("book.json",'wb')
    def process_item(self,item,spider):
        content=json.dumps(dict(item),ensure_ascii=False)+',\n'
        self.f.write(content.encode("utf-8"))
        return item
    def close_spider(self,spider):
        self.f.close()
'''
class BookCsvPipeline(object):
    def __init__(self):
        self.f=open("book.csv",'w',encoding='utf-8')
        self.writer=csv.writer(self.f)
    def process_item(self,item,spider):
        print(item)
        textlist=[item['author'],item['bookname'],item['status'],item['update_time'],item['latest_chapter_name'],item['book_introduction']]
        self.writer.writerow(textlist)
        return item
    def close_spider(self,spider):
        self.f.close()
'''

class MysqlPipeline(object):
    def __init__(self):
        self.conn=pymysql.connect('localhost','root','mysql','mysql',charset='utf8')
        self.cursor=self.conn.cursor()
    def process_item(self,item,spider):
        self.cursor.execute("use scraping")
        insert_sql="""
        INSERT INTO book(author,bookname,status,book_introduction,update_time,latest_chapter_name) VALUES(%s,%s,%s,%s,%s,%s)
        """
        self.cursor.execute(insert_sql,(item['author'],item['bookname'],item['status'],item['book_introduction'],item['update_time'],item['latest_chapter_name']))
        self.conn.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

