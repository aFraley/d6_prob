from pygal import Bar
from dice import Dice
from tqdm import tqdm

# Create a dice object
die1 = Dice()
die2 = Dice()

# Store the results in a list.
results = [die1.roll() + die2.roll() for i in tqdm(range(1000000))]

# Store the frequencies of results in a list.
frequencies = [results.count(i) for i in range(2, die1.num_sides * 2 + 1)]

# Visualize the results.
hist = Bar()

hist.title = 'Results of rolling 2d6 1,000,000 times.'
hist.x_labels = [i for i in range(2, die1.num_sides * 2 + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('2d6', frequencies)
hist.render_to_file('test.svg')
