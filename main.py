from matplotlib import pyplot
from strategy import RandomStrategy, AscendingStrategy, CopyingStrategy, ConstantStrategy
from simulation import Simulation

# Top-level code, handling creation of Strategy objects,
# carrying out the simulation and creating & saving statistics.
# Creates stats of strategies' probability of winning as a function of number of rounds per game.

# "constants"
SAMPLES 	= 10 	# Number of samples (= number of games to simulate).
MIN_ROUNDS 	= 1		# Number of rounds per game to start simulation from.
MAX_ROUNDS	= 100	# Number of rounds per game to end simulation at.

plot_folders = ["wins", "losses", "ties"]

opponents = [RandomStrategy, AscendingStrategy, CopyingStrategy, ConstantStrategy]
for strat0 in range(4):
	strategy0 = opponents[strat0]() # Creates first player with strategy code strat0.
	
	# Containers for statistical data
	stats_wins = []
	stats_losses = []
	stats_ties = []
	
	# Set color cycles for each plot
	for p in range(3):
			pyplot.figure(plot_folders[p])
			pyplot.gca().set_color_cycle(['red', 'green', 'blue', 'orange'])
	
	# Simulate against each strategy
	for strat1 in range(4):
		strategy1 = opponents[strat1]() # Creates second player with appropriate class (strategy type).
		print "Strategy {0} v. strategy {1}".format(strat0, strat1)
		
		sim = Simulation(strategy0, strategy1)
		stats_wins.append([])
		stats_losses.append([])
		stats_ties.append([])
		for rounds in range(MIN_ROUNDS, MAX_ROUNDS + 1):
			# Simulate set number of games and save stats of wins, losses and ties for each 
			results = sim.simulate(SAMPLES, rounds)
			wins = results.count(0)
			losses = results.count(1)
			ties = results.count(-1)
			
			stats_wins[strat1].append(float(wins)/SAMPLES)
			stats_losses[strat1].append(float(losses)/SAMPLES)
			stats_ties[strat1].append(float(ties)/SAMPLES)
		
		# Save all stats to a container for easy distribution to plots
		stats = [stats_wins, stats_losses, stats_ties]
		# Plot results to a plot
		for p in range(3):
			pyplot.figure(plot_folders[p])
			pyplot.plot(range(MIN_ROUNDS, MAX_ROUNDS + 1), stats[p][strat1])
	
	# Design each plot and save it to a PNG file
	plot_titles = ["Probability of winning", "Probability of losing", "Probability of game being tied"]
	for prob in range(3):
		pyplot.figure(plot_folders[prob])
		pyplot.title("Strategy {0} - {1}, {2} samples".format(strat0, plot_titles[prob], SAMPLES))
		pyplot.xlabel("Number of rounds")
		pyplot.ylabel(plot_titles[prob])
		pyplot.xlim([MIN_ROUNDS, MAX_ROUNDS])
		pyplot.ylim([-0.005, 1.005])
		pyplot.legend(['v. {0}'.format(strat) for strat in range(4)], loc='best')
		pyplot.savefig('../output/{0}/strategy{1}_{2}-{3}rounds_{4}samples.png'.format(plot_folders[prob], strat0, MIN_ROUNDS, MAX_ROUNDS, SAMPLES))
		pyplot.draw()
		pyplot.clf()
