import random

random.seed(1)


def heads_or_tails():
    flip = random.randint(0, 1)
    if flip == 0:
        return ("heads")
    elif flip == 1:
        return ("tails")
    # flips = []
    # while number_of_flips >0:
    #     number_of_flips -= 1
    #     flip = random.randint(0,1)
    #     flips.append(flip)
    # # print(flips)
    # for i in flips:
    #     if i == 0:
    #         print("heads")
    #     elif i == 1:
    #         print("tails")
    # return flips


if __name__ == '__main__':
    random.seed(1)
    number_of_flips = int(input())
    # flips = []
    while number_of_flips > 0:
        number_of_flips -= 1
        print(heads_or_tails())
    #     flips.append(x)
    # for i in flips:
    #     print(i)

    # for i in heads_or_tails(number_of_flips):
    #     if i == 1:
    #         print("heads")
    #     elif i == 0:
    #         print("tails")
    # print(heads_or_tails(number_of_flips))