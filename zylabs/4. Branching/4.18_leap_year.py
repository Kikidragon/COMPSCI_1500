is_leap_year = False

year = int(input())
# print(year % 400)
# print(year % 4)
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(year, "- leap year")
        else:
            print(year, "- not a leap year")
    else:
        print(year, "- leap year")
else:
    print(year, "- not a leap year")