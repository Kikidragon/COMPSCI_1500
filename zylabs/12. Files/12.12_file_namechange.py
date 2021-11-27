name = input()
f = open(str(name))
file = f.readlines()
for i in file:
    i = i.strip('\n')
    i = i.replace("photo.jpg", "info.txt")
    print(i)