import math
miles_gallon = float(input())
dollars_gallon = float(input())
miles_20 = (dollars_gallon / miles_gallon) * 20
miles_75 = (dollars_gallon / miles_gallon) * 75
miles_500 = (dollars_gallon / miles_gallon) * 500
#print(miles_20, miles_75, miles_500)
print('{:.2f} {:.2f} {:.2f}'.format(miles_20, miles_75, miles_500))