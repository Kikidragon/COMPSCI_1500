import math
count = 0
try:
    int1 = int(input())
    count +=1
    int2 = int(input())
    count +=1
    int3 = int(input())
    count +=1
    list1 = (int1, int2, int3)
    print("{}".format(max(list1)))
except EOFError:
    print("{} input(s) read:".format(count))
    if count == 0:
        print("No max")
    elif count == 1:
        print("Max is {}".format(int1))
    elif count == 2:
        list1 = (int1, int2)
        print("Max is {}".format(max(list1)))
