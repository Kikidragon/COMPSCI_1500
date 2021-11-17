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


def rolling_for_pair(d1, d2, val):
    count = 0
    z = 0
    while z == 0:
        x = d1.roll()
        y = d2.roll()
        # print(x, y)
        if x == val and y == val:
            count +=1
            break
        else:
            count +=1
    return count


if __name__ == "__main__":
    die1 = GVDie()  # Create a GVDie object
    die2 = GVDie()  # Create a second GVDie object
    die1.set_seed(15)  # Set the first GVDie object with seed value 15
    die2.set_seed(15)  # Set the second GVDie object with seed value 15

    val = int(input())
    rolls = rolling_for_pair(die1, die2, val)  # Should return the number of rolls to reach total.
    print('It took {} rolls to get a pair of {}\'s.'.format(rolls, val))