import numpy as np
from numpy.random import default_rng

rng = default_rng()

def no_doubling_game(initial_bet = 25):
	two_dice_total = np.sum(rng.integers(low = 0, high = 7, size = 2))

	if two_dice_total == 7 or two_dice_total == 12:
		winnings = initial_bet * 2
	else:
		winnings = 0

	return winnings

def doubling_game(initial_bet = 25):
	two_dice_total = np.sum(rng.integers(low = 0, high = 7, size = 2))

	if two_dice_total == 7 or two_dice_total == 12:
		winnings = initial_bet * 2
	else:
		total_bet = initial_bet * 2
		extra_dice = rng.integers(low = 0, high = 7, size = 1)

		three_dice_total = two_dice_total + extra_dice[0]

		if three_dice_total == 12:
			winnings = total_bet * 2
		else:
			winnings = 0

	return winnings

def simulate_non_doubling_game(initial_bet = 25, n_games = 1000):
	winnings_array = np.zeros(n_games)

	for i in range(n_games):
		winnings_array[i] = no_doubling_game(initial_bet)

	expected_return = np.mean(winnings_array)

	profit = expected_return - initial_bet

	if profit > 0:
		print(f"The non-doubling game makes a profit of {profit} gold on average, against a bet of {initial_bet} gold.")
	else:
		print(f"The non-doubling game makes a loss of {profit} gold on average, against a bet of {initial_bet} gold.")

def simulate_doubling_game(initial_bet = 25, n_games = 1000):
	winnings_array = np.zeros(n_games)

	for i in range(n_games):
		winnings_array[i] = doubling_game(initial_bet)

	expected_return = np.mean(winnings_array)

	profit = expected_return - initial_bet

	if profit > 0:
		print(f"The doubling game makes a profit of {profit} gold on average, against a bet of {initial_bet} gold.")
	else:
		print(f"The doubling game makes a loss of {profit} gold on average, against a bet of {initial_bet} gold.")

simulate_non_doubling_game(n_games = 100000)
simulate_doubling_game(n_games = 100000)