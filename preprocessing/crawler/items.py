# -*- coding: utf-8 -*-

""" Contains the Models used by the scraper

August 20, 2016
"""

import scrapy

class SeedItem(scrapy.Item):
    """ An element in the SeedDB table. """

    link = scrapy.Field()
    name = scrapy.Field()
