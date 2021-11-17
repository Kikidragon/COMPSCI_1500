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


def roll_specific_number(die, num, goal):
    x = 0
    count = 0
    while x < goal:
        y = die.roll()
        count += 1
        if y == num:
            x += 1
    return count


# tails = 0
# count = 0
# while tails < goal:
#     x = gv_coin.flip()
#     count += 1
#     if x != 1:
#         tails += 1
#     else:
#         continue
# return count

if __name__ == "__main__":
    die = GVDie()  # Create a GVDie object
    die.set_seed(15)  # Set the GVDie object with seed value 15

    num = int(input())
    goal = int(input())
    rolls = roll_specific_number(die, num, goal)  # Call roll_specific_number() and return number of rolls.
    print('It took {} rolls to get a \"{}\" {} times.'.format(rolls, num, goal))
#