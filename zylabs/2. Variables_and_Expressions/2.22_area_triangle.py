import math

''' Type your code here. '''
#s(s-a)(s-b)(s-c)
a = float(input())
b = float(input())
c = float(input())

d = (a + b + c)
s = d / 2
area1 = s * ((s - a) * (s - b) * (s - c))
area = math.sqrt(area1)


print("The area of the triangle is: {:.3f}".format(area))
