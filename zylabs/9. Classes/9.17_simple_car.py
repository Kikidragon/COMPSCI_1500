class SimpleCar:
    def __init__(self):
        self.miles = 0

    def drive(self, dist):
        self.miles = self.miles + dist

    def reverse(self, dist):
        self.miles = self.miles - dist

    def get_odometer(self):
        return self.miles

    def honk_horn(self):
        print('beep beep')

    def report(self):
        print('Car has driven: {} miles'.format(self.miles))


if __name__ == "__main__":
    car = SimpleCar()

    more = int(input())
    less = int(input())

    car.drive(more)
    car.reverse(less)

    car.honk_horn()
    car.report()
# Create SimpleCar object
# Drive input number of miles forward
# Drive input number of miles in reverse
# Honk the horn
# Report car status
