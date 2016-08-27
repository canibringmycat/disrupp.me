# -*- coding: utf-8 -*-

""" Here be the data pipelines the scraped text get passed through.

August 20, 2016
"""

from scrapy.exceptions import DropItem
import re

class ReducePipeline(object):
    """ Reduces the fields of each SeedItem down to one element """

    def process_item(self, item, spider):
        if len(item['name']) == 1 and len(item['link']) == 1:
            item['name'] = item['name'][0]
            item['link'] = item['link'][0]
        else:
            print(">>> {0}".format(item['name']))
            print(">>> {0}".format(item['link']))
            raise DropItem("Too many names/links: {0}".format(item))
        return item


class DuplicatesPipeline(object):
    """ Removes duplicate companies """

    def __init__(self):
        self.companies_seen = set()
        self.link_seen = set()

    def process_item(self, item, spider):
        if item['name'] in self.companies_seen or item['link'] in self.link_seen:
            raise DropItem("Duplicate item found: {0}".format(item))
        else:
            self.companies_seen.add(item['name'])
            self.link_seen.add(item['link'])
            return item


class TextCleanerPipeline(object):
    """ Place all text cleaning rules here. """

    def process_item(self, item, spider):
        self.clean_whitespace(item)
        self.clean_mysteries(item)
        return item

    def clean_whitespace(self, item):
        """ Removes surrounding white space in company names. """
        item['name'] = item['name'].strip()

    def clean_mysteries(self, item):
        """ Removes the [???] some companies have in their name. """
        if "[???]" in item['name']:
            item['name'] = item['name'][6:]


class TextFilterPipeline(object):
    """ Remove all text based on rules inserted here. """

    def process_item(self, item, spider):
        self.filter_stealth(item)
        return item

    def filter_stealth(self, item):
        """ Removes all YC Stealth startups """
        pattern = re.compile("YC[\\w\\s]*Stealth")
        if pattern.match(item['name']):
            raise DropItem("Stealth YC found: {0}".format(item))
