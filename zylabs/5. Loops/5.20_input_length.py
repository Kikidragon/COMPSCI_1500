user_text = input()
num = len(user_text)
for c in user_text:
    if c == ' ' or c == '.' or c == '!' or c == ',':
        num -= 1
        continue
print(num)


