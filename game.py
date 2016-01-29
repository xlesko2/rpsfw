from strategy import Strategy

# Class representing a game (= series of rounds).
class Game:
	def __init__(self, strategies):
		# List of participating strategies (players).
		# Note: While game is currently built for two competing players, 
		#		 this setup allows easy extension for more than two players.
		self.strategies = strategies
		
		# List of round results (for statistical purposes).
		self.round_history = list()
	
	
	
	# Note: Modification to list of moves needed in case of
	#		extending the game for more than two players.
	# Returns:
	#		-1 tie
	#		 0 move1 wins
	#		 1 move2 wins
	def decide_winner(self, move0, move1):
		# DEBUG start
		if not (move0 in range(0, 5)):
			raise ValueError("move0 not in range 0-4", move0)
		elif not (move1 in range(0, 5)):
			raise ValueError("move1 not in range 0-4", move1)
		# DEBUG end
		if move0 == move1:	# Tie
			return -1
		
		# Moves are marked as smaller & larger, to avoid duplicate conditions.
		if move0 < move1:
			smaller = move0
			larger = move1
		else:
			smaller = move1
			larger = move0
		
		# Actual determining of winner according to the rules of the game.
		if smaller == 0:
			if (larger == 2) or (larger == 3):
				winner = smaller
			else:
				winner = larger
		
		# Conditions for smaller number being 1 or 2 happen to be the same,
		# as both moves win over move 4, both lose to move 3,
		# and move 2 wins over move 1, which is covered in the else statement.
		elif (smaller == 1) or (smaller == 2):
			if larger == 4:
				winner = smaller
			else:
				winner = larger
		
		# Move 3 loses to move 4 and move 4 cannot be the 'smaller' move,
		# therefore we have no other situation where the smaller number wins.
		else:
			winner = larger
			
		# Now, we map the winner and loser back to move0 and move1.
		if winner == move0:
			return 0
		else:
			return 1
	
	# Simulation of a single round of play.
	def play_round(self):
		move0 = self.strategies[0].choose_move()
		move1 = self.strategies[1].choose_move()
		
		self.strategies[0].last_move = move0
		self.strategies[0].opp_last_move = move1
		self.strategies[1].last_move = move1
		self.strategies[1].opp_last_move = move0
		
		winner = self.decide_winner(move0, move1)
		self.round_history.append(winner)
		
		return winner
	
	# Simulation of a whole game (essentially a series of rounds).
	def play_game(self, rounds):
		self.round_history = [] # Clear history
		
		# Clear strategies' memory
		for s in self.strategies:
			s.reset()
		
		# Simulate particular rounds
		ties = 0
		for r in range(rounds):
			winner = self.play_round()
			
			if winner == -1:
				ties += 1
			else:
				self.strategies[winner].score += 1
		
		# Determine and return the overall winner
		results = {ties: -1}
		for s in range(len(self.strategies)):
			results.update({self.strategies[s].score: s})
		return results[max(results)]
