nums = input()
s = nums.split()

if len(s) > 9:
    print("Too many inputs")
else:
    y = int(len(s) / 2)
    mid = s[y]
    print(mid)

# s = input()
# y = int(len(s)/2)
# mid2 = s[y]
# mid1 = s[y-1]
# mid3 = s[y+1]
