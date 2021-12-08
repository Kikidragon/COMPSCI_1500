#it works but not recursion
def draw_triangle(base):
    x = base
    y = ('{base:' '^20}'.format(base=base * '*'))
    print(y.rstrip())
    while base >= 0:
        base -= 1
        x -=2
        if x <= 0:
            break
        else:
            z = ('{base:' '^20}'.format(base=x * '*'))
            print(z.rstrip())
# x = 1
# z = 20
# y = ('{base:' '^20}'.format(base=x * '*'))
# print(y.rstrip())
# while x < base:
#     x += 2
#     z = ('{base:' '^20}'.format(base=x * '*'))
#     print(z.rstrip())
if __name__ == '__main__':
    base_length = int(input())
    draw_triangle(base_length)