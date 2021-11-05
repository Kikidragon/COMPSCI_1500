class VendingMachine:
    def __init__(self):
        self.bottles = 20

    def purchase(self, amount):
        self.bottles = self.bottles - amount

    def restock(self, amount):
        self.bottles = self.bottles + amount

    def get_inventory(self):
        return self.bottles

    def report(self):
        print('Inventory: {} bottles'.format(self.bottles))


if __name__ == "__main__":

    vending = VendingMachine()

    vending.bottles = 20

    less = int(input())
    more = int(input())

    vending.purchase(less)
    vending.restock(more)
    vending.get_inventory()
    vending.report()


# Create VendingMachine object
# Purchase input number of drinks
# Restock input number of bottles
# Report inventory
