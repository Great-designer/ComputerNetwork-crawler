from scrapy import cmdline
# 在爬虫运行过程中，会自动将状态信息存储在crawls/storeMyRequest目录下，支持续爬
cmdline.execute('scrapy crawl craw'.split())
