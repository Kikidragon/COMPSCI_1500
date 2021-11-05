class Calculator:
    def __init__(self):
        self.value = 0.0

    def add(self, val):
        self.value = val + self.value

    def subtract(self, val):
        self.value = self.value - val

    def multiply(self, val):
        self.value = val * self.value

    def divide(self, val):
        self.value = self.value / val

    def clear(self):
        self.value = 0.0

    def get_value(self):
        return self.value


if __name__ == "__main__":

    calc = Calculator()
    num1 = float(input())
    num2 = float(input())

    # 1. The initial value
    print('{:.1f}'.format(calc.get_value()))

    # 2. The The value after adding num1
    calc.add(num1)
    print('{:.1f}'.format(calc.get_value()))

    # 3. The value after multiplying by 3
    calc.multiply(3)
    print('{:.1f}'.format(calc.get_value()))

    # 4. The value after subtracting num2
    calc.subtract(num2)
    print('{:.1f}'.format(calc.get_value()))

    # 5. The value after dividing by 2
    calc.divide(2)
    print('{:.1f}'.format(calc.get_value()))

    # 6. The value after calling the clear() method
    calc.clear()
    print('{:.1f}'.format(calc.get_value()))
