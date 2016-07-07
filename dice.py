from random import randint


class Dice:
    """A class to represent dice."""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        """Return a random number representing dice rolls."""
        return randint(1, self.num_sides)

