def calc_toll(hour=0.0, is_morning=False, is_weekend=False):
    if is_weekend == True:
        if hour < 7 and is_morning == True:
            price = 1.05
        elif 7 <= hour < 8 and is_morning == True:
            price = 2.15
        else:
            price = 1.10
    elif is_weekend == False:
        if hour < 7 and is_morning == True:
            price = 1.15
        elif 7 <= hour < 10 and is_morning == True:
            price = 2.95
        elif hour > 10 and is_morning == True:
            price = 1.9
        elif hour < 3 and is_morning == False:
            price = 1.9
        elif 3 <= hour < 8 and is_morning == False:
            price = 3.95
        else:
            price = 1.4
    return '{:.2f}'.format(price)


if __name__ == '__main__':
    calc_toll(8, True, False)
    print('{:.2f}'.format(calc_toll(8, True, False)))
    print('{:.2f}'.format(calc_toll(1, False, False)))
    print('{:.2f}'.format(calc_toll(3, False, True)))
    print('{:.2f}'.format(calc_toll(5, True, True)))