# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# from scrapy.loader import ItemLoader
# from scrapy.loader.processors import TakeFirst


# class FlightLoader(ItemLoader):
#     # 自定义itemLoader,用于存储爬虫所抓取的字段内容
#     default_output_processor = TakeFirst()


class FlightItem(scrapy.Item):  # 建立相应的字段
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()  # 进港或出港
    number = scrapy.Field()  # 航班号
    origin = scrapy.Field()  # 始发地
    destination = scrapy.Field()  # 目的地
    pick_up = scrapy.Field()  # 接机楼
    boarding = scrapy.Field()  # 乘机楼
    expect = scrapy.Field()  # 预计
    actual = scrapy.Field()  # 实际
    state = scrapy.Field()  # 状态
