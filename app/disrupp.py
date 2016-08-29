""" Contains all code related to the name-generation model.
	- generates industry-specific Markov models

Created: August 27, 2016
"""

import utils
import random
import json

class StartupGenerator(object):
	def __init__(self, order=3, json_file, industry):
		# initialize startup generator here
		with open(json_file) as json_data:
			data = json.load(json_data)
		self.model = MarkovModel(order, data[industry])

	def generate(self):
		self.model.start()
		return self.model.generate()


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
		for i in (len(self.data) - 1):
			self.training_set.append(self.prefix + self.data[i] + self.terminator)

	def generate(self, firstname, lastname, industry):
		# Random Number Generator
		random.seed(firstname + lastname)
		print("printing random: " + random.random())


