''' Type your code here. '''
import math
x = int(input())
y = 2 ** (1 / 12)
x1 = x * y
x2 = x1 * y
x3 = x2 * y
x4 = x3 * y

print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(x, x1, x2, x3, x4))