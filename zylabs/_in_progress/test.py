stop = 16
total = 0
for number in [5, 4, 4, 5, 4, 6]:
    print(number, end=' ')
    total += number
    if total >= stop:
        print('@')
        break
else:
    print('| {}'.format(total))
print('done')