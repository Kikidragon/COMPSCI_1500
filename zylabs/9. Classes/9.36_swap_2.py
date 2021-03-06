class Number:
    def __init__(self, n):
        self.num = n

    def get_num(self):
        return self.num

    def set_num(self, n):
        self.num = n


def swap(num1, num2):
    # num3 = num1
    # num1 = num2
    # num2 = num3
    # Number.num1, Number.num2 = num2.get_num(), num1.get_num()  # returns Number object
    # num1, num2 = num2.get_num(), num1.get_num() -> returns int
    get_1 = num1.get_num()
    get_2 = num2.get_num()
    num1 = num1.set_num(get_2)
    num2 = num2.set_num(get_1)
    # print("num1", num1)
    # print("num2", num2)
    # return num1, num2


if __name__ == "__main__":
    int1 = int(input())
    int2 = int(input())

    num1 = Number(int1)
    num2 = Number(int2)

    swap(num1, num2)
    print('num1 =', num1.get_num(), 'and num2 =', num2.get_num())
