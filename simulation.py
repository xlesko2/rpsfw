from game import Game

# Class representing a simulation (series of games).
# Requires pre-created Strategy (= player) objects.
class Simulation:
	def __init__(self, strategy0, strategy1):
		self.game = Game([strategy0, strategy1])
		self.game_history = []
		return None
	
	# Method simulating required number of games
	# and returning statistics as a list of winners.
	def simulate(self, number_of_games, rounds_per_game):
		self.game_history = [] # Clear history
		
		for g in range(number_of_games):
			current = self.game.play_game(rounds_per_game)
			self.game_history.append(current)
		
		return self.game_history
