import math

''' Type your code here. '''
'''Volume = πr2h
Area = 2πrh + 2πr2'''
r = float(input())
h = float(input())

v = math.pi * (r * r) * h
sa = (2 * math.pi * r * h) + (2 * math.pi * (r * r))

print('Volume: {:.1f} cubic inches'.format(v))
print('Surface area: {:.1f} square inches'.format(sa))