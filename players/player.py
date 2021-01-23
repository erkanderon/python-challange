class Player:

	def __init__(self, name, word_type):

		# word_type: refers to whether it is consonant or vowel
		# values: c or v

		self.name = name
		self.word_type = word_type
		self.score = 0

	def calculate_score(self, words):

		for i in set(words):
			count = words.count(i)
			words = list(filter((i).__ne__, words))
			self.score = self.score + count