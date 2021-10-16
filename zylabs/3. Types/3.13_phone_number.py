phone_number = int(input())

''' Type your code here. '''

first = phone_number // 10000000
mid = phone_number // 10000 % 1000
end =phone_number % 10000

print("({0}) {1}-{2}".format(first, mid, end))