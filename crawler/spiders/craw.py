import scrapy

from crawler.items import FlightItem


class CrawSpider(scrapy.Spider):
    name = 'craw'  # 用于区别Spider
    allowed_domains = ['data.carnoc.com/corp/airport/fra__airportflight.html']  # 允许访问的域
    start_urls = ['http://data.carnoc.com/corp/airport/fra__airportflight.html']  # 爬取的地址

    def parse(self, response, **kwargs):  # 爬取方法
        item = FlightItem()
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        # 先获取每个课程的div
        for box in response.xpath('//div[@id="icefable1"]/li'):
            item['type'] = '进港'  # 进港
            item['number'] = box.xpath('.//span[@class="flt_no"]/text()').extract()[0].strip()  # 获取div中的航班号
            item['origin'] = box.xpath('.//span[@class="flt_city"]/text()').extract()[0].strip()  # 获取div中的始发地
            item['pick_up'] = box.xpath('.//span[@class="terminal"]/text()').extract()[0].strip()  # 获取div中的接机楼
            item['expect'] = box.xpath('.//span[last()-2]/text()').extract()[0].strip()  # 获取div中的预计
            item['actual'] = box.xpath('.//span[last()-1]/text()').extract()[0].strip()  # 获取div中的实际
            item['state'] = box.xpath('.//span[last()]/text()').extract()[0].strip()  # 获取div中的状态
            yield item  # 返回信息
        item = FlightItem()
        for box in response.xpath('//div[@id="icefable2"]/li'):
            item['type'] = '出港'  # 进港
            item['number'] = box.xpath('.//span[@class="flt_no"]/text()').extract()[0].strip()  # 获取div中的航班号
            item['destination'] = box.xpath('.//span[@class="flt_city"]/text()').extract()[0].strip()  # 获取div中的目的地
            item['boarding'] = box.xpath('.//span[@class="terminal"]/text()').extract()[0].strip()  # 获取div中的乘机楼
            item['expect'] = box.xpath('.//span[last()-2]/text()').extract()[0].strip()  # 获取div中的预计
            item['actual'] = box.xpath('.//span[last()-1]/text()').extract()[0].strip()  # 获取div中的实际
            item['state'] = box.xpath('.//span[last()]/text()').extract()[0].strip()  # 获取div中的状态
            yield item  # 返回信息
