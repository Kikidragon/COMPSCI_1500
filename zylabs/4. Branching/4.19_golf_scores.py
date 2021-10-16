par = int(input())
stroke = int(input())

if 1 < par < 6 and stroke == par - 2:
    print("Eagle")
elif 1 < par < 6 and stroke == par - 1:
    print("Birdie")
elif 1 < par < 6 and stroke == par:
    print("Par")
elif 1 < par < 6 and stroke == par + 1:
    print("Bogey")
else:
    print("Error")