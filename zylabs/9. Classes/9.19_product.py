class Product:
    def __init__(self, code, price, count):
        self.code = code
        self.price = price
        self.count = count

    def set_code(self, code):
        self.code = code

    def get_code(self):
        return self.code

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_count(self, count):
        self.count = count

    def get_count(self):
        return self.count

    def add_inventory(self, amt):
        self.count = self.count + amt

    def sell_inventory(self, amt):
        self.count = self.count - amt


if __name__ == "__main__":
    name = 'Apple'
    price = 0.40
    num = 3
    p = Product(name, price, num)

    # Test 1 - Are instance attributes set/returned properly?
    print('Name:', p.get_code())
    print('Price: {:.2f}'.format(p.get_price()))
    print('Count:', p.get_count())

    # Test 2 - Are attributes set/returned properly after adding and selling?
    num = 10
    p.add_inventory(num)
    num = 5
    p.sell_inventory(num)
    print('Name:', p.get_code())
    print('Price: {:.2f}'.format(p.get_price()))
    print('Count:', p.get_count())

    # Test 3 - Do setters work properly?
    name = 'Golden Delicious'
    p.set_code(name)
    price = 0.55
    p.set_price(price)
    num = 4
    p.set_count(num)
    print('Name:', p.get_code())
    print('Price: {:.2f}'.format(p.get_price()))
    print('Count:', p.get_count())
