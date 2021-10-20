# item_name = input('Enter food item name:\n')

# Finish reading item price and quantity, then output a receipt

# Read in a second food item name, price, and quantity, then output a second receipt

# Add a gratuity and total with tip to the second receipt

'''Enter food item name:
hot dog
Enter item price:
2.00
Enter item quantity:
5

RECEIPT
5 hot dog @ $2.00 = $10.00
Total cost: $10.00'''

item = input("Enter food item name:")
print()
price = float(input("Enter item price:"))
print()
amt = float(input("Enter item quantity:"))
print()
print()
print("RECEIPT")
print(int(amt), item, "@ ${:.2f}".format(price), "= ${:.2f}".format(price * amt))
print("Total cost: ${:.2f}".format(price * amt))
print()
print()
item2 = input("Enter second food item name:")
print()
price2 = float(input("Enter item price:"))
print()
amt2 = float(input("Enter item quantity:"))
print()
print()
total = (price * amt) + (price2 * amt2)
print("RECEIPT")
print(int(amt), item, "@ ${:.2f}".format(price), "= ${:.2f}".format(price * amt))
print(int(amt2), item2, "@ ${:.2f}".format(price2), "= ${:.2f}".format(price2 * amt2))
print("Total cost: ${:.2f}".format(total))
print()
tip = total * 0.15
new_total = total + tip
print("15% gratuity: ${:.2f}".format(tip))
print("Total with tip: ${:.2f}".format(new_total))