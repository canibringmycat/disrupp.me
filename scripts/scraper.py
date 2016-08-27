from bs4 import BeautifulSoup
import requests
import re
from urllib2 import urlopen

# Websites to scrape names from
# http://yclist.com/
# http://angelpad.org/
# http://www.techstars.com/companies/

# def get_startup_names(site_url):
# 	startup_names = []
# 	html = urlopen(site_url).read()
# 	# soup = BeautifulSoup(html, "lxml")
# 	# container = soup.find("..., ...")
# 	# startup_names = []
#     return startup_snames

websites = ["http://yclist.com/", "http://angelpad.org/", "http://www.techstars.com/companies/"]

complete_directory = []

# for website in websites:
# 	r = urlopen(website).read()
# 	soup = BeautifulSoup(r)
# 	print(soup)
	# curr_list = get_startup_names(website)
	# complete_directory.append(curr_list)

# YCombinator List
content = urlopen(websites[0]).read()
soup = BeautifulSoup(content, "lxml")
gdata = soup.find_all("td")
lst = []
# prev_item = "not_a_link"

print(soup.get_text())
print(type(soup.get_text()))
print(soup.td.contents.prettify())

	# item_string = item_string.rstrip('\n')
	# item_string = item_string.strip()

	# lst.append(item.text)
	# if (item.text[:2] == "htt"):
	# 	print(item.text)
	# 	lst.append(prev_item)
	# prev_item = item.text



# for start_up in complete_directory:
# 	print(start_up)







