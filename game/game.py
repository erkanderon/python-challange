
import random
from players.player import Player


class Game:

	def __init__(self, word):
		self.p1 = Player("David", "c")
		self.p2 = Player("Rogers", "v")
		self.game_word = word
		self.subs = self.divide_strings_into_subs(self.game_word)
		self.seperate_subs(self.subs)

	def start(self):
		self.p1.calculate_score(self.consonants)
		self.p2.calculate_score(self.vowels)
		print(self.p1.name, self.p1.score)
		print(self.p2.name, self.p2.score)
		self.result()

	def divide_strings_into_subs(self, word):
		res = [word[i: j].upper() for i in range(len(word)) for j in range(i + 1, len(word) + 1)]
		return res

	def seperate_subs(self, ty):
		vows = ["A", "E", "I", "O", "Ö", "İ", "U", "Ü"]
		cons = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
		
		self.vowels = []
		self.consonants = []

		for i in ty:
			if i[0] in vows:
				self.vowels.append(i)
			elif i[0] in cons:
				self.consonants.append(i)
			else:
				continue

	def result(self):
		if self.p1.score > self.p2.score:
			print("The Winner is " + self.p1.name + " with " + str(self.p1.score - self.p2.score) + " difference")
		elif self.p2.score > self.p1.score:
			print("The Winner is " + self.p2.name + " with " + str(self.p2.score - self.p1.score) + " difference")
		else:
			print("Draw")	