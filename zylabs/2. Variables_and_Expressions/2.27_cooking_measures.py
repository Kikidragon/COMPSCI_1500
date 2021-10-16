# lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))

# FIXME (1): Finish reading other items into variables, then output the three ingredients

# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients

# FIXME (3): Convert and output the ingredients from (2) to gallons

'''Enter amount of lemon juice (in cups):
2
Enter amount of water (in cups):
16
Enter amount of agave nectar (in cups):
2.5
How many servings does this make?
6

Lemonade ingredients - yields 6.00 servings
2.00 cup(s) lemon juice
16.00 cup(s) water
2.50 cup(s) agave nectar'''

lemon = float(input("Enter amount of lemon juice (in cups):"))
print()
water = float(input("Enter amount of water (in cups):"))
print()
agave = float(input("Enter amount of agave nectar (in cups):"))
print()
servings = float(input("How many servings does this make?"))
print()
print()

print("Lemonade ingredients - yields", "{:.2f}".format(servings), "servings")
print("{:.2f}".format(lemon), "cup(s) lemon juice")
print("{:.2f}".format(water), "cup(s) water")
print("{:.2f}".format(agave), "cup(s) agave nectar")
print()

like = float(input("How many servings would you like to make?"))
print()
print()
lemon2 = (lemon / servings) * like
water2 = (water / servings) * like
agave2 = (agave / servings) * like

print("Lemonade ingredients - yields", "{:.2f}".format(like), "servings")
print("{:.2f}".format(lemon2), "cup(s) lemon juice")
print("{:.2f}".format(water2), "cup(s) water")
print("{:.2f}".format(agave2), "cup(s) agave nectar")
print()

print("Lemonade ingredients - yields", "{:.2f}".format(like), "servings")
print("{:.2f}".format(lemon2 / 16), "gallon(s) lemon juice")
print("{:.2f}".format(water2 / 16), "gallon(s) water")
print("{:.2f}".format(agave2 / 16), "gallon(s) agave nectar")
