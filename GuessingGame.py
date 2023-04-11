import math
import random

import matplotlib.pyplot as plt


def generate_gaussian_data(sigma, n):
    return [random.gauss(0, sigma) for i in range(n)]


def plot_histogram(data, num_bars):
    min_val = min(data)
    max_val = max(data)
    range_val = max_val - min_val
    bar_width = range_val / num_bars
    bins = [min_val + bar_width * i for i in range(num_bars + 1)]
    plt.hist(data, bins=bins)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Random Gaussian Data')
    plt.show()


class Sim:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.wins = 0
        self.losses = 0
        self.max = 0
        self.min = 0

    def simulate_game(self, sigma):
        # Generate random numbers for a, b, and k
        a = random.randint(self.lower_bound, self.upper_bound)
        b = random.randint(self.lower_bound, self.upper_bound)
        k = random.gauss(mu=0, sigma=sigma)

        if k > self.max:
            self.max = k
        if k < self.min:
            self.min = k

        # Determine the outcome of the game
        if a > k:
            if a > b:
                self.wins += 1
            else:
                self.losses += 1
        else:
            if a > b:
                self.losses += 1
            else:
                self.wins += 1


if __name__ == "__main__":
    # the larger this number the greater range of possibilities for k
    sigma = 5000

    # how coarsely the distribution should be displayed, higher = finer
    num_bars = 100

    # number of times to run the simulation
    iterations = 10 ** 6

    # define the lower and upper bound for the a and b guess
    # These are uniformly distributed they DO NOT follow a bell curve
    lower_bound = -1000
    upper_bound = 1000

    # create our sim
    sim = Sim(lower_bound, upper_bound)

    # run the sim
    for i in range(iterations):
        sim.simulate_game(sigma)

    # Print the results
    print(f"Wins: {sim.wins}")
    print(f"Losses: {sim.losses}")
    print(f"Win Ratio: {sim.wins / iterations:.2%}")

    print(f"Max k: {sim.max:.2f}")
    print(f"Min k: {sim.min:.2f}")

    # show the distribution of the guesses k
    data = generate_gaussian_data(sigma, iterations)
    plot_histogram(data, num_bars)
