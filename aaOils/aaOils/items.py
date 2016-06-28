# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy

class OilItem(scrapy.Item):
    # define the fields for your item here like:

    #网址
    htmlUrl = scrapy.Field()
    #图片url
    imgSrc = scrapy.Field()
    #精油名称
    oilName = scrapy.Field()
    #价格范围
    priceRange = scrapy.Field()
    #具体价格及容量
    prices = scrapy.Field()
    #描述
    description = scrapy.Field()
    #种类
    species = scrapy.Field()
    #来源地
    origin = scrapy.Field()
    #提取方式
    extraction_process = scrapy.Field()
    #香味级别
    perfume_note = scrapy.Field()
