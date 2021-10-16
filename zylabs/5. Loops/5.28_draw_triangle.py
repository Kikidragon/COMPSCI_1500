triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
a = 1
print('')
height = triangle_height
# print (triangle_char + " ")
# print (triangle_char + " " + triangle_char + " ")
# print (triangle_char + " " + triangle_char + " " + triangle_char + " ")
while a <= triangle_height:
    z = a
    while z != 0:
        print(triangle_char, end=' ')
        z -= 1
    print()
    a += 1
    # if height == triangle_height:
    #     print(triangle_char + " ")
    #     a += 1
    # else:

