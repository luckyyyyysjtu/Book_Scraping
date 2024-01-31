# -*- coding: utf-8 -*-
import scrapy
from quotes.items import QuotesItem

class QuotesbotSpider(scrapy.Spider):
    name = 'bookbot'
    '''
    allowed_domains = ['www.quanshuwang.com']
    baseURL = 'http://www.quanshuwang.com/page/'
    offset=1
    '''
    start_urls=['http://www.quanshuwang.com/list/5_1.html']




    def parse(self, response):

        book_detail_page_links=response.css(".l.mr10")
        yield from response.follow_all(book_detail_page_links,self.parse_book_detail)

        pagination_links=response.css('a.next')
        yield from response.follow_all(pagination_links,self.parse)


    def parse_book_detail(self,response):
        def extract_with_css(query):
            return  response.css(query).get(default='').strip()

        item = QuotesItem()

        item['author']=extract_with_css('meta[property="og:novel:author"]::attr(content)')
        item['bookname']=extract_with_css('meta[property="og:novel:book_name"]::attr(content)')
        item['status']=extract_with_css('meta[property="og:novel:status"]::attr(content)')
        item['update_time']= extract_with_css('meta[property="og:novel:update_time"]::attr(content)')
        item['latest_chapter_name']= extract_with_css('meta[property="og:novel:latest_chapter_name"]::attr(content)')
        item['book_introduction']=extract_with_css('#waa')

        yield item




'''
        if self.offset < 10:
            self.offset += 1
            url=self.baseURL+str(self.offset)
            yield scrapy.Request(url,callback=self.parse)

'''