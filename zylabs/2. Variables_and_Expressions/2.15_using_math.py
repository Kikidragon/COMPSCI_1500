import math
''' Type your code here. '''
#print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3, your_value4))

x = float(input())
y = float(input())
z = float(input())

x_pow_z = x ** z
x_pow_yz = x ** (pow(y,z))
abs_x_y = math.fabs(x - y)
sqrt_x_z = math.sqrt(x ** z)

print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(x_pow_z, x_pow_yz, abs_x_y, sqrt_x_z))