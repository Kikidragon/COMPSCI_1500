# FIXME UNIFNISHED
import random


class GVDie:
    def __init__(self):
        # set default values
        self.my_value = random.randint(1, 6)
        self.rand = random.Random()

    def roll(self):
        self.my_value = self.rand.randint(1, 6)

        # set the random number generator seed for testing

    def set_seed(self, seed):
        self.rand.seed(seed)

    # allows dice to be compared if necessary
    def compare_to(self, other):
        return self.my_value - d.my_value


def roll_total(die, total):
    pass

# Type your code here

if __name__ == "__main__":
    die = GVDie()  # Create a GVDie object
    die.set_seed(15)  # Set the GVDie object with seed value 15

    total = int(input())
    rolls = roll_total(die, total)  # Should return the number of rolls to reach total.
    print('Number of rolls to reach at least {}: {}'.format(total, rolls))