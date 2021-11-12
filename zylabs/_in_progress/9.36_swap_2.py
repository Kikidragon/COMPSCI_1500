# FIXME UNFINISHED
class Number:
    def __init__(self, n):
        self.num = n

    def get_num(self):
        return self.num

    def set_num(self, n):
        self.num = n

def swap(num1, num2):
    pass
    # Type your code here


if __name__ == "__main__":
    int1 = int(input())
    int2 = int(input())

    num1 = Number(int1)
    num2 = Number(int2)

    swap(num1, num2)
    print('num1 =', num1.get_num(), 'and num2 =', num2.get_num())
