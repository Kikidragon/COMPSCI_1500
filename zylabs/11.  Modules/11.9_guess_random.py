import random
def number_guess(num):
    x = random.randint(1,100)
    if num == x:
        print("{} is correct!".format(num))
    elif num > x:
        print("{} is too high. Random number was {}.".format(num, x))
    elif num < x:
        print("{} is too low. Random number was {}.".format(num, x))


if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)

    # Convert the string tokens into integers
    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        num = int(token)
        number_guess(num)
