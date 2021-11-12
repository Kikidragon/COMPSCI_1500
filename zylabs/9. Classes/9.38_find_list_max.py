import random


class Numbers:
    def __init__(self):
        self.nums = []

    def get_nums(self):
        return self.nums

    def set_nums(self, nums):
        self.nums = []
        self.nums = nums[:]

    def find_max(self):
        maximum = 0
        for i in self.nums:
            if i > maximum:
                maximum = i
        return maximum

    def fill_randomly(self, seed, size):
        self.nums = []
        random.seed(seed)
        for index in range(size):
            self.nums.append(random.randint(0, 1000))


if __name__ == "__main__":
    my_numbers = Numbers()
    my_numbers.fill_randomly(7, 10)  # Fill nums with 10 pseudo-random numbers using seed value 7
    print(my_numbers.get_nums())
    print(my_numbers.find_max())
