""" Contains all code related to the generating industry-specific Markov models.

Created: August 28, 2016
"""

class MarkovModel(object):
	def __init__(self, order=3, t_data):
		training_set = []
		start_sequence = "_" * order
		# initialize model here
		for i in (len(t_data) - 1):
			training_set.append(start_sequence + t_data[i])
