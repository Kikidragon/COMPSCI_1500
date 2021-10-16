import math


def feet_to_steps(user_feet):
    steps = user_feet / 2.5
    steps = math.floor(steps)
    return steps


if __name__ == '__main__':
    feet1 = float(input())
    print('{:.0f}'.format(feet_to_steps(feet1)))