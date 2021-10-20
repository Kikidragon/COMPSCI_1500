# Finish reading another word and an integer into variables.
# Output all the values on a single line
color = input('Enter favorite color:\n')
pet = input('Enter pet\'s name:\n')
number = input('Enter a number:\n')

print("You entered:", color, pet, number)
print()

pass1 = color + "_" + pet
pass2 = number + color + number

print("First password:", pass1)
print("Second password:", pass2)
print()



print("Number of characters in " + pass1 + ":", len(pass1))
print("Number of characters in " + pass2 + ":", len(pass2))


#  Output two password options
'''password1 = favorite_color
print('\nFirst password:')'''


#  Output the length of the two password options



