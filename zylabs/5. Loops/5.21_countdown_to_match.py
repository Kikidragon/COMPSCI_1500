num = int(input())
num2 = num
while num > 0:
    if num == 11:
        print(11)
        break
    if 10 > num or num >= 100:
        print("Input must be 11-100")
        break
    elif num == num2:
        print(num)
        num -= 1
        if num == 11 or num == 22 or num == 33 or num == 44 or num == 55 or num == 66 or num == 77 or num == 88 or num == 99:
            break
    else:
        print(num)
        num -= 1
        if num == 11 or num == 22 or num == 33 or num == 44 or num == 55 or num == 66 or num == 77 or num == 88 or num == 99:
            print(num)
            break
