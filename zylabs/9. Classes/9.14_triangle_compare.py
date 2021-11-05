class Triangle:
    def __init__(self):
        self.base = 0.0
        self.height = 0.0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height

    def get_area(self):
        area = 0.5 * self.base * self.height
        return area

    def print_info(self):
        print('Base: {:.2f}'.format(self.base))
        print('Height: {:.2f}'.format(self.height))
        print('Area: {:.2f}'.format(self.get_area()))


if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()

    triangle1.base = float(input())
    triangle1.height = float(input())
    a1 = triangle1.get_area()
    triangle2.base = float(input())
    triangle2.height = float(input())
    a2 = triangle2.get_area()
    if a1 > a2:
        print('Triangle with larger area:')
        print("Base: {:.2f}".format(triangle1.base))
        print("Height: {:.2f}".format(triangle1.height))
        print("Area: {:.2f}".format(a1))
    else:
        print('Triangle with larger area:')
        print("Base: {:.2f}".format(triangle2.base))
        print("Height: {:.2f}".format(triangle2.height))
        print("Area: {:.2f}".format(a2))

    # Read and set base and height for triangle1 (use set_base() and set_height())

    # Read and set base and height for triangle2 (use set_base() and set_height())

    # Determine larger triangle (use get_area())

    # print('Triangle with larger area:')

