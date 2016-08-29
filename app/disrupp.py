""" Contains all code related to the name-generation model.
	- generates industry-specific Markov models

Created: August 27, 2016
"""

import utils
import random
import json

class StartupGenerator(object):
	def __init__(self, order=3, json_file, firstname, lastname, industry):
		# initialize startup generator here
		with open(json_file) as json_data:
			data = json.load(json_data)
		# json file
		# --> key: industry name
		# --> value: list of startup names
		self.model = MarkovModel(order, data[industry])

	def generate(self):
		self.model.start()
		return self.model.generate(firstname, lastname)


class MarkovModel(object):
	def __init__(self, order=3, t_data):
		self.order = order
		self.data = t_data
		self.training_set = []
		self.prefix = ""
		self.terminator = "*" #terminating character

	def start(self):
		self.prefix = "_" * self.order
		# initialize model here
		for i in range(len(self.data)):
			self.training_set.append(self.prefix + self.data[i] + self.terminator)

	def generate(self, firstname, lastname):
		# Random Number Generator
		random.seed(firstname + lastname)
		print("printing random: " + random.random())


	def add_to_dict(dictionary, elem):
		if elem in dictionary:
			dictionary[elem] += 1
		else:
			dictionary[elem] = 1

	def find_next(prefix, word):
		if prefix not in word:
			return []
		start = word.index(prefix)
		return [word[start + 3]] + find_next(prefix, word[(start + 1):])


	# to be placed somewhere in the generate function
	seen = {'total': 0} # next letters and total occurences - to calculate probability

	for word in self.training_set:
		if self.prefix in word:
			next_list = find_next(self.prefix, word)
			for elem in next_list:
				add_to_dict(seen, elem)
				seen['total'] += 1




