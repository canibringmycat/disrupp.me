""" Contains all code related to the name-generation model.
	- generates industry-specific Markov models

Created: August 27, 2016
"""

import utils

class StartupGenerator(object):
	def __init__(self):
		# write code here

class MarkovModel(object):
	def __init__(self, order=3, t_data):
		training_set = []
		start_sequence = "_" * order
		# initialize model here
		for i in (len(t_data) - 1):
			training_set.append(start_sequence + t_data[i])
