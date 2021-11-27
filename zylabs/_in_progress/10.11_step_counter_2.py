# FIXME UNFINISHED
import math


def steps_to_miles(step):
    if step < 0:
        raise ValueError
    else:
        miles = step / 2000
        # miles = math.floor(miles)
        return miles


if __name__ == '__main__':
    try:
        step = float(input())
        print('{:.2f}'.format(steps_to_miles(step)))
    except ValueError:
        print("Exception: Negative step count entered.")
