# FIXME UNFINISHED
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
    def compare_To(self, other):
        return self.my_value - d.my_value


def roll_specific_times(die, rolls):
    total = 0
    while rolls > 0:
        rolls -= 1
        x = die.roll()
        total += x
    return total

# FIXME it says the die.roll isnt right type check if its being used right


if __name__ == "__main__":
    die = GVDie()  # Create a GVDie object
    die.set_seed(15)  # Set the GVDie object with seed value 15

    rolls = int(input())  # Get the number of rolls
    total = roll_specific_times(die, rolls)  # Should return the total sum after the number of rolls.
    print('{} rolls return a total of {}.'.format(rolls, total))