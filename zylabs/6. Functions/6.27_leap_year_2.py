def is_leap_year(user_year):
    if user_year == 1900:
        return False
    elif (user_year % 4) == 0 or (user_year % 100) == 0 or (user_year % 400) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    year = int(input())
    leap = is_leap_year(year)
    if leap == True:
        print('{} is a leap year.'.format(year))
    else:
        print('{} is not a leap year.'.format(year))

# if (year % 4) == 0:
#     if (year % 100) == 0:
#         if (year % 400) == 0:
#             print(year, "- leap year")
#         else:
#             print(year, "- not a leap year")
#     else:
#         print(year, "- leap year")
# else:
#     print(year, "- not a leap year")ear")