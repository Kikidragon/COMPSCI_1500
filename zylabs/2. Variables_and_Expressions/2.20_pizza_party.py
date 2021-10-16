import math

''' Type your code here. '''
people = int(input())

slices = people * 2
pizzas = math.ceil(people / 6)
# cans = math.ceil(paint)


price = pizzas * 14.95

print("Pizzas:", pizzas)
print('Cost: ${:.2f}'.format(price))