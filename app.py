from game.game import Game

class Main:

	def __init__(self):
		pass

	def enter_game_word(self):
		self.ch = input("Enter the Game Word: ")

		if type(self.ch) is not str:
			print("Please enter a string")
			self.enter_game_word()

		if self.ch != self.ch.upper():
			print("Please enter uppercase")
			self.enter_game_word()

		if len(self.ch) < 1 or len(self.ch) > 10:
			print("The word cannot be 0 or bigger than 10")
			self.enter_game_word()

		return self.ch

if __name__ == "__main__":
	game_word = Main().enter_game_word()
	game = Game(game_word)
	game.start()

