# FIXME UNFINSHED
from random import randint
class RandomNumbers:
    def __init__(self):
        self.var1 = 0
        self.var2 = 0
        self.var3 = 0

    def get_var1(self, var1):
        self.var1 = var1

    def get_var2(self, var2):
        self.var2 = var2

    def get_var3(self,var3):
        self.var3 = var3

    def set_random_values(self):
        pass

    def get_random_values(self):
        pass


if __name__ == "__main__":
    low = int(input())
    high = int(input())

    numbers = RandomNumbers()
    numbers.set_random_values(low, high)
    numbers.get_random_values()