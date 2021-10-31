input_string = []
while True:
    line = input()
    if 'quit' in line:
        break
    else:
        input_string.append(line)

for line in input_string:
    a,b = line.split(' ')
    print(f'Eating {b} {a} a day keeps the doctor away.')

# enter = input()
# value2 = enter.split()
# values = []
# values.extend(value2)
# while value2[0] != "quit":
#     value = input()
#     value2 = value.split()
#     values.extend(value2)
# print(values)
# for x in enumerate(values):
#     print("Eating {} {} a day keeps the doctor away.".format(x, x))



# numint = int(input())
# values = []
# while numint > 0:
#     numint -= 1
#     value = int(input())
#     values.append(value)
# threshold = int(input())
# for value in values:
#     if value <= threshold:
#         print(value, end=',')
#     else:
#         continue