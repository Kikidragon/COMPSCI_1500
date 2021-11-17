import random


class GVDie:
    def __init__(self):
        # set default values
        self.my_value = random.randint(1, 6)
        self.rand = random.Random()

    def roll(self):
        self.my_value = self.rand.randint(1, 6)
        return self.my_value

        # set the random number generator seed for testing

    def set_seed(self, seed):
        self.rand.seed(seed)

    # allows dice to be compared if necessary
    def compare_to(self, other):
        return self.my_value - d.my_value


def roll_total(die, total):
    die_tot = 0
    count = 0
    while die_tot < total:
        x = die.roll()
        # print(die_tot)
        die_tot += x
        count += 1
        # print(x)
        # print(die_tot)
        # print(count)
    return count
    # die_tot = 0
    # while total > 0:
    #     x = die.roll(i)
    #     die_tot += x
    #     total -= 1
    # return die_tot


if __name__ == "__main__":
    die = GVDie()  # Create a GVDie object
    die.set_seed(15)  # Set the GVDie object with seed value 15

    total = int(input())
    rolls = roll_total(die, total)  # Should return the number of rolls to reach total.
    print('Number of rolls to reach at least {}: {}'.format(total, rolls))