""" Contains all code related to the name-generation model.
	- generates industry-specific Markov models

Created: October 23, 2016
"""

import random


class MarkovModel():
	def __init__(self, t_data, order=3):
		self.order = order
		self.data = t_data
		self.training_set = []
		self.prefix = ""
		self.terminator = "*" #terminating character
		self.final_name = ""
		self.history = {}

	# loads all training data into the model's training_set
	# each word is added as _ _ _ h e l l o *
	# starting prefix, word, terminating character
	def start(self):
		self.prefix = "_" * self.order
		# initialize model here
		for i in range(len(self.data)):
			self.training_set.append(self.prefix + self.data[i] + self.terminator)

	def train_word(self, word):
		for i in range(len(word)-1):
			curr = word[i]
			next = word[i+1]
			char_dict = self.history.setdefault(curr, {next: 0})
			char_dict.setdefault(next, 0)
			char_dict[next] += 1


	def generate(self, firstname, lastname):
		# Random Number Generator
		random.seed(firstname + lastname)
		print("printing random: " + str(random.random()))

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
	# seen = {'total': 0} # next letters and total occurences - to calculate probability

	# for word in self.training_set:
	# 	if self.prefix in word:
	# 		next_list = find_next(self.prefix, word)
	# 		for elem in next_list:
	# 			add_to_dict(seen, elem)
	# 			seen['total'] += 1

	# buckets = []
	# decimal = 0
	# for letter in seen.keys():
	# 	decimal += seen[letter] / seen['total']
	# 	buckets += [[letter, decimal]]

	# generate a random number and map to next state
	# rando = 0 # random number generated by RNG

	def find_bucket(rando, buckets):
		for bucket in buckets:
			if rando <= bucket[1]:
				return bucket[0]

	# next_letter = find_bucket(rando, buckets)
	# self.prefix = self.prefix[1:] + next_letter # new prefix, repeat
	# self.final_name += next_letter



test = MarkovModel(["hello", "world", "sam", "choi"])
test.start()
print(test.training_set)
test.generate("hello", "world")




