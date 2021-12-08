#it works but not recursion
def draw_triangle(base):
    # print(base * '*')
    x = 1
    z=20
    y = ('{base:' '^20}'.format(base=x * '*'))
    print(y.rstrip())
    while x < base:
        x+=2
        z = ('{base:' '^20}'.format(base=x*'*'))
        print(z.rstrip())


    # for each iteration -2 and replace with spaces)
    # while base > 0:
    #     print(base*'*')
    # base_list = []
    # while base > 0:
    #     base -= 2
    #     base_list.append(base)
    # y = len(base_list)
    # while len(base_list) < 0:
    #     del base_list[0]
    #     x = base_list.pop()
    #     print('*')
    #     z = y-len(base_list) +1
    #     print((' ' * z), (base * '*'), (' ' * z))
    #     print("{}{}{}".format(z*' ', base*'*', z*' '))

    #
    # if base >= 0:
    #     print(base * '*')
    # else:
    #     base1 = int(base)-2
    #     base3 = '*'*base1
    #     base4 = ' '+base3+' '
    #     print(base4)
    #     draw_triangle(base1)

        # x = base * '*'
        # x[0].replace('*', ' ')
        # x[base-1].replace('*', ' ')
        # draw_triangle(base-2)


if __name__ == '__main__':
    base_length = int(input())
    draw_triangle(base_length)