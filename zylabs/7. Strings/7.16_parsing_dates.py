# FIXME UNFINISHED
def get_month_as_int(monthString):
    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0

    return month_int


user_string = 0
enter = []
while user_string != '-1':
    user_string = input()
    enter.append(user_string)
    if user_string == '-1':
        enter.pop()

for i in enter:
    if ',' in i:
        # print(i)
        split_comma = i.split(',')
        month_day = split_comma[0].split()
        month = get_month_as_int(month_day[0])
        day = month_day[1]
        year = split_comma[1].strip()
        print("{}/{}/{}".format(month, day, year))

    else:
        continue
# month / day / year
# print(enter)


