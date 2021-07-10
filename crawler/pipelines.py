# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime
import os

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import json

checkFile = "isRunning.txt"
startDate = datetime.datetime.now().strftime('%m.%d')
log_file = f"data{startDate}.json"


class CrawlerPipeline(object):
    def __init__(self):
        # 打开文件
        self.file = open(log_file, 'w', encoding='utf-8')

    # 该方法用于处理数据
    def process_item(self, item, spider):
        # 读取item中的数据
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # 写入文件
        self.file.write(line)
        # 返回item
        return item

    # 该方法在spider被开启时被调用。
    @staticmethod
    def open_spider(spider):
        f = open(checkFile, "w")  # 创建一个文件，代表爬虫在运行中
        f.close()

    # 该方法在spider被关闭时被调用。
    @staticmethod
    def close_spider(spider):
        is_file_exist = os.path.isfile(checkFile)
        if is_file_exist:
            os.remove(checkFile)
