arrow_base_height = int(input('Enter arrow base height:\n'))

arrow_base_width = int(input('Enter arrow base width:\n'))

arrow_head_width = int(input('Enter arrow head width:\n'))

while arrow_head_width <= arrow_base_width:
    arrow_head_width = int(input('Enter arrow head width:\n'))
print()

a = 0
b = arrow_base_width
while a != arrow_base_height:
    b = arrow_base_width
    while b > 0:
        print('*', end='')
        b -= 1
    print()
    a+=1


c = arrow_head_width
while c != 0:
    y = c
    while y != 0:
        print('*', end='')
        y -= 1
    print()
    c -= 1


# while a <= triangle_height:
#     z = a
#     while z != 0:
#         print(triangle_char, end=' ')
#         z -= 1
#     print()
#     a += 1
