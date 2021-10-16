user_input = input()
inputs = []
print(user_input[::-1])

inputs.append(user_input)
while (user_input != 'done') and (user_input != "Done") and (user_input != "d"):
    user_input = input()
    inputs.append(user_input)
    if (user_input != "done") and (user_input != "Done") and (user_input != "d"):
        print(user_input[::-1])
# print(inputs)