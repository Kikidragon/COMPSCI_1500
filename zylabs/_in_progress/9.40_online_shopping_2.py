# FIXME UNFINISHED: 7/29
class ItemToPurchase:
    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def print_item_cost(self):
        print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, self.item_price, self.item_quantity*self.item_price))
        # return self.item_price

    def print_item_description(self):
        print("{}: {}".format(self.item_name, self.item_description))
        # print description for item to purchase object


class ShoppingCart:
    def __init__(self, name='none', date="January 1, 2016", cart=[]):
        self.customer_name = name
        self.current_date = date
        self.cart_items = cart

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
        # add item to cart_items list, param ItemToPurchase, no return

    def remove_item(self, name):
        if name in self.cart_items:
            self.cart_items.remove(name)
        else:
            print("Item not found in cart. Nothing removed.")
        # remove item from cart_items list, param ItemToPurchase, no return
        # if not found print("Item not found in cart. Nothing removed.")
        pass

    def modify_item(self, ItemToPurchase):
        if ItemToPurchase in self.cart_items:
            pass
        else:
            print("Item not found in cart. Nothing modified.")
        # change item quantity, param ItemToPurchase, no return
        # if not found print("Item not found in cart. Nothing modified.")
        pass

    def get_num_items_in_cart(self):
        return len(self.cart_items)
        # returns len(cart_items), no params

    def get_cost_of_cart(self):
        # finds and returns cost of all items in cart_items, no params
        pass

    def print_total(self):
        # print total of obj in cart
        print("OUTPUT SHOPPING CART")
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Number of items: {}".format(len(self.cart_items)))
        if len(self.cart_items) > 0:
            print()
            total = 0
            for item in self.cart_items:
                print("{} {} @ ${} = ${}".format(item.item_name, item.item_quantity, item.item_price, item.item_quantity*item.item_price))
                total += item.item_quantity * item.item_price
            print("Total: ${}".format(total))
        else:
            print("SHOPPING CART IS EMPTY")
            print("Total: $0")

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
        print("ADD ITEM TO CART")
        add = ItemToPurchase()
        add.item_name = input("Enter the item name:\n")
        add.item_description = input("Enter the item description:\n")
        add.item_price = int(input("Enter the item price:\n"))
        add.item_quantity = int(input("Enter the item quantity:\n"))
        ShoppingCart.add_item(cart, add)
    elif choice == 'r':
        print("REMOVE ITEM FROM CART")
        remove = input("Enter name of item to remove:\n")
        ShoppingCart.remove_item(cart, remove)
    elif choice == 'c':
        print("CHANGE ITEM QUANTITY")
        change = ItemToPurchase()
        change.item_name = input("Enter the item name:\n")
        change.item_quantity = int(input("Enter the new quantity:\n"))
        ShoppingCart.modify_item(cart, change)
    elif choice == 'i':
        return ShoppingCart.print_descriptions(cart)
    elif choice == 'o':
        return ShoppingCart.print_total(cart)


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
            choice = input("Choose an option:\n")
        else:
            while choice != 'q':
                choice = input("Choose an option:\n")
                if choice == 'a' or choice == 'r' or choice == 'c' or choice == 'i' or choice == 'o':
                    for i in execute_menu(choice, cart):
                        print(i, end='')
                    print()
    # cart.print_total()




    # item1 = ItemToPurchase()
    # print("Item 1")
    # item1.item_name = input("Enter the item name:\n")
    # item1.item_price = int(input("Enter the item price:\n"))
    # item1.item_quantity = int(input("Enter the item quantity:\n"))
    # print()
