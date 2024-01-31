# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author=scrapy.Field()
    bookname=scrapy.Field()
    status=scrapy.Field()
    update_time=scrapy.Field()
    latest_chapter_name=scrapy.Field()
    book_introduction=scrapy.Field()

