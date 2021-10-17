user_input = input()
hourly_temperature = user_input.split()
counter = len(hourly_temperature)
for i in hourly_temperature:
    counter -= 1
    if counter > 0:
        print(i, "-> ", end='')
    else:
        print(i, end=' ')
        print()

