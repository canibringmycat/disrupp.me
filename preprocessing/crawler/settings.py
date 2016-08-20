# -*- coding: utf-8 -*-

# Scrapy settings for crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Pipelines enabled
ITEM_PIPELINES = {
    'crawler.pipelines.ReducePipeline' : 100,
    'crawler.pipelines.TextFilterPipeline' : 200,
    'crawler.pipelines.TextCleanerPipeline' : 300,
    'crawler.pipelines.DuplicatesPipeline' : 400
}
