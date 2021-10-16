num = int(input())
num2 = int(input())

if num2 < num:
    print("Second integer can't be less than the first.")

if num <= num2:
    print(num, end=' ')
    while num < num2:
        num = num + 5
        if num <= num2:
            print(num, end=' ')
    print()