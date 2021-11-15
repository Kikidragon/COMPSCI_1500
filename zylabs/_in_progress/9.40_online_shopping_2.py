# FIXME UNFINISHED: 4/29
class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_cost(self):
        print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, self.item_price, self.item_quantity*self.item_price))
        # return self.item_price

    def print_item_description(self):
        print("{}: {}".format(self.item_name, self.item_description))
        # print description for item to purchase object


class ShoppingCart:
    def __init__(self):
        self.customer_name = "none"
        self.current_date = "January 1, 2016"
        self.cart_items = []

    def add_item(self):
        # add item to cart_items list, param ItemToPurchase, no return
        pass

    def remove_item(self):
        # remove item from cart_items list, param ItemToPurchase, no return
        # if not found print("Item not found in cart. Nothing removed.")
        pass

    def modify_item(self):
        # change item quantity, param ItemToPurchase, no return
        # if not found print("Item not found in cart. Nothing modified.")
        pass

    def get_num_items_in_cart(self):
        # returns len(cart_items), no params
        pass

    def get_cost_of_cart(self):
        # finds and returns cost of all items in cart_items, no params
        pass

    def print_total(self):
        # print total of obj in cart
        print("OUTPUT SHOPPING CART")
        if len(self.cart_items) > 0:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of items: {}".format(len(self.cart_items)))
            print()
            total = 0
            for item in self.cart_items:
                print("{} {} @ ${} = ${}".format(item.item_name, item.item_quantity, item.item_price, item.item_quantity*item.item_price))
                total += item.item_quantity * item.item_price
            print("Total: ${}".format(total))
        else:
            print("SHOPPING CART IS EMPTY")

    def print_descriptions(self):
        # print each item's description
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Number of items: {}".format(len(self.cart_items)))
        print()
        for item in self.cart_items:
            print("{}: {}".format(item.item_name, item.item_description))



def print_menu():
    # prints a menu
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    pass


def execute_menu(choice, cart):
    # executes menu
    if choice == 'a':
        # add_item()
        return 'a'
    elif choice == 'r':
        # remove_item()
        return 'r'
    elif choice == 'c':
        # modify_item()
        return 'c'
    elif choice == 'i':
        # print_descriptions()
        return 'i'
    elif choice == 'o':
        # print_total()
        return 'o'


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.customer_name = input("Enter customer's name:\n")
    cart.current_date = input("Enter today's date:\n")
    print()
    print("Customer name: {}".format(cart.customer_name))
    print("Today's date: {}".format(cart.current_date))
    print()
    print_menu()
    print()
    choice = input("Choose an option:\n")
    while choice != 'q':
        if choice == 'a' or choice == 'r' or choice == 'c' or choice == 'i' or choice == 'o':
            for i in execute_menu(choice, cart):
                print(i, end='')
            print()
            print()
            print_menu()
            print()
            choice = input("Choose an option:\n")
        else:
            while choice != 'q':
                print()
                print_menu()
                print()
                choice = input("Choose an option:\n")
                print()
                if choice == 'a' or choice == 'r' or choice == 'c' or choice == 'i' or choice == 'o':
                    for i in execute_menu(choice, cart):
                        print(i, end='')
                    print()

    # item1 = ItemToPurchase()
    # print("Item 1")
    # item1.item_name = input("Enter the item name:\n")
    # item1.item_price = int(input("Enter the item price:\n"))
    # item1.item_quantity = int(input("Enter the item quantity:\n"))
    # print()
