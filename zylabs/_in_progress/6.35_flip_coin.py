import random


def heads_or_tails(number_of_flips):
    flips = []
    while number_of_flips > 0:
        number_of_flips -= 1
        flip = random.randint(0, 1)
        flips.append(flip)
    for i in flips:
        if i == 1:
            return "heads"
        elif i == 0:
            return "tails"
    # return flips


if __name__ == '__main__':
    random.seed(1)
    number_of_flips = int(input())

    for i in heads_or_tails(number_of_flips):
        if i == 1:
            print("heads")
        elif i == 0:
            print("tails")
    # print(heads_or_tails(number_of_flips))