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

######################
# Central Tendencies #
######################
def mean(x):
    """Determine the mean result."""
    return str(sum(x) / len(x))



def median(v):
    """Determine the median result."""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        # if odd, return the middle value
        return str(sorted_v[midpoint])
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return str((sorted_v[lo] + sorted_v[hi]) / 2)


def quantile(x, p):
    """Determine a value based on its percentage."""
    p_index = int(p * len(x))
    return str(sorted(x)[p_index])


##############
# Dispersion #
##############
def data_range(x):
    return str(max(x) - min(x))

# Execute tests and save the results.
with open('data.txt', 'w') as f:
    f.write('Two D6 Analysis')
    f.write('\nMean result: ' + mean(results))
    f.write('\nMedian result: ' + median(results))
    f.write('\nQuantile result: ' + quantile(results, .90))
    f.write('\nData Range: ' + data_range(results))


# Visualize the results.
hist = Bar()

hist.title = 'Results of rolling 2d6 1,000,000 times.'
hist.x_labels = [i for i in range(2, die1.num_sides * 2 + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('2d6', frequencies)
hist.render_to_file('test.svg')
