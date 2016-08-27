from bs4 import BeautifulSoup
import requests

class Scraper(object):

	def __init__(self, url):
		""" Initializes the Scraper to scrape from the provided url. """
		self.url = url

	def soupify(self):
		""" Returns a BeautifulSoup instance on the html for self.url """
		response = requests.get(self.url)
		soup = BeautifulSoup(response.content, "html.parser")
		return soup

	def dump(self, names, out_file):
		with open(out_file, 'w') as f:
			for elem in names:
				f.write("{0}\n".format(elem))


class YCScraper(Scraper):

	def __init__(self):
		""" Initializes the Scraper to scrape YCombinator. """
		url = "http://yclist.com/"
		super(YCScraper, self).__init__(url)

	def parse_startups(self):
		""" LOL this is such a hack. """
		soup = self.soupify()
		results = soup.find_all(lambda tag : tag.name == 'tr' and tag.has_attr('class'))
		names = []
		for elem in results:
			children = [c for c in elem.children]
			names += children[3].contents
		return names

class AngelPadScraper(Scraper):

	def __init__(self):
		url = "http://angelpad.org/"
		super(AngelPadScraper, self).__init__(url)

	def parse_startups(self):
		# TODO implement
		pass



class TechStarsScraper(Scraper):
	def __init__(self):
		url = "http://www.techstars.com/companies/"
		super(TechStarsScraper, self).__init__(url)

	def parse_startups(self):
		# TODO implement
		pass
