from random import randrange

# Class representing a single player in the game, defined by its strategy code.
class Strategy:
	def __init__(self):
		# -1 setting has no particular meaning and is overwritten in first round.
		self.last_move = -1			# Own last move
		self.opp_last_move = -1		# Opponent's last move
		self.score = 0				# Number of games won
		
		return None
	
	# Method for choosing the next move of the player,
	# based on its strategy code.
	def choose_move(self): # fallback; implemented in inheriting classes
		return randrange(0, 5)
	
	# Reset strategy's 'memory' (e. g., before new game start).
	def reset(self):
		self.last_move = -1
		self.opp_last_move = -1
		self.score = 0

class RandomStrategy(Strategy):
	def choose_move(self):
		return randrange(0,5)

class AscendingStrategy(Strategy):
	def choose_move(self):
		if self.last_move == -1:
			return randrange(0, 5)
		else:
			return (self.last_move + 1) % 5

class CopyingStrategy(Strategy):
	def choose_move(self):
		if self.opp_last_move == -1:	# First round of the game
			return randrange(0, 5)
		else:
			return self.opp_last_move

class ConstantStrategy(Strategy):
	def choose_move(self):
		if self.last_move == -1:		# First round of the game
			return randrange(0, 5)
		else:
			return self.last_move
