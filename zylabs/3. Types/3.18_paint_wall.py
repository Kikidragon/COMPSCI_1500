import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
height = int(input('Enter wall height (feet):\n'))
width = int(input('Enter wall width (feet):\n'))
area = height * width
print('Wall area:', area, "square feet")

paint = area / 350

print("Paint needed: {:.2f} gallons".format(paint))

cans = math.ceil(paint)

print("Cans needed:", cans, "can(s)")
# a gallon of paint covers 350 square feet.

print()
the_color = input("Choose a color to paint the wall:\n")
if the_color == 'red':
    the_cost = paint_colors['red'] * cans
if the_color == 'blue':
    the_cost = paint_colors['blue'] * cans
if the_color == 'green':
    the_cost = paint_colors['green'] * cans
print("Cost of purchasing", the_color, "paint: ${:.0f}".format(the_cost))

# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall

# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer

# FIXME (4): Calculate and output the total cost of paint can needed depending on color
