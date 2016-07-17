from bs4 import BeautifulSoup
import requests
import re
from urllib2 import urlopen

# Websites to scrape names from
# http://yclist.com/
# http://angelpad.org/
# http://www.techstars.com/companies/

def get_startup_names(site_url):
	startup_names = []
	html = urlopen(site_url).read()
	# soup = BeautifulSoup(html, "lxml")
	# container = soup.find("..., ...")
	# startup_names = []
    return startup_names

websites = ["http://yclist.com/", "http://angelpad.org/", "http://www.techstars.com/companies/"]

complete_directory = []

for website in websites:
	curr_list = get_startup_names(website)
	complete_directory.append(curr_list)

