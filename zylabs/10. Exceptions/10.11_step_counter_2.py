
def steps_to_miles(step):
    if step < 0:
        raise ValueError("Exception: Negative step count entered.")
    return step / 2000
        # miles = math.floor(miles)


if __name__ == '__main__':
    step = int(input())
    try:
        x = steps_to_miles(step)
        print('{:.2f}'.format(x))
    except ValueError as e:
        print(e)