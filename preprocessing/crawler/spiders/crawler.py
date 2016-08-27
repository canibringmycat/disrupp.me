""" Contains the spider object that crawls seed-db

August 20, 2016
"""

from crawler.items import SeedItem
from scrapy import Spider, Request

class SeedSpider(Spider):
    """ A Spider object that crawls Seed-DB. """

    name = "seed_db"
    allowed_domains = ["seed-db.com"]
    start_urls = ["http://www.seed-db.com/accelerators"]

    def parse(self, response):
        for sel in response.xpath("//a"):
            link_matches = sel.xpath("@href").extract()
            name_matches = sel.xpath("strong/text()").extract()
            if len(link_matches) > 0 and len(name_matches) > 0:
                item = SeedItem()
                item['link'] = link_matches
                item['name'] = name_matches
                yield item
            for link in link_matches:
                if "/accelerators/" in link and "/accelerators/all" not in link:
                    yield Request("http://www.seed-db.com{0}".format(link), callback=self.parse)
