title = input("Enter a title for the data:\n")
print("You entered: {}".format(title))
print()
header1 = input("Enter the column 1 header:\n")
print("You entered: {}".format(header1))
print()
header2 = input("Enter the column 2 header:\n")
print("You entered: {}".format(header2))
print()
data = input("Enter a data point (-1 to stop input):\n")
data_list = []
while data != '-1':
    if data == '-1':
        break
    elif ',' not in data:
        print("ERROR: No comma in string.")
    # elif (data.find(',') != -1) and (data.rfind(',') != -1):
    #     print("ERROR: Too many commas in input.")
    else:
        # data = data.replace(' ', '')
        data_split = data.split(',')
        y = data_split[1]
        y = y.replace(' ', '')
        if not y.isdigit():
            print("ERROR: Comma not followed by an integer.")
        else:
            data_point = {data_split[0]: data_split[1]}
            data_list.append(data_point)
            print("Data string: {}".format(data_split[0]))
            print("Data integer: {}".format(data_split[1]))
    data = input("Enter a data point (-1 to stop input):\n")

print('{title:' '^43}'.format(title=title))
print('{col1:' '<20} | {col2:' '>23}'.format(col1=header1, col2=header2))
print("----------------------------------------------")
print(data_list)
# for i in data_list:
#     print('{data:' '<20} | {int:' '>23}'.format(data=i[0], int=i[1]))


