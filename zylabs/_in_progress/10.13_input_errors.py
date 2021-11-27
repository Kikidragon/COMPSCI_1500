# FIXME UNFINISHED
try:
    int1 = int(input())
    int2 = int(input())
    int3 = int(input())
    inputs = [int1, int2, int3]
    count = len(inputs)
    print(max(inputs))
except EOFError:
    print("{} input(s) read:".format(count))
    if count != 0:
        print("Max is {}".format(max(inputs)))
    else:
        print("No max")
