input_month = input()
input_day = int(input())

# The dates for each season are:
# Spring: March 20 - June 20
# Summer: June 21 - September 21
# Autumn: September 22 - December 20
# Winter: December 21 - March 19

if input_day <= 0 or input_day > 31 or (input_day > 28 and input_month == 'February') or (
        input_day > 30 and input_month == 'September'):
    print("Invalid")

elif (input_month == 'March' and input_day >= 20) or input_month == 'April' or input_month == 'May' or (
        input_month == 'June' and input_day <= 20):
    print("Spring")

elif (input_month == 'June' and input_day >= 21) or input_month == 'July' or input_month == 'August' or (
        input_month == 'September' and input_day <= 21):
    print("Summer")

elif (input_month == 'September' and input_day >= 22) or input_month == 'October' or input_month == 'November' or (
        input_month == 'December' and input_day <= 20):
    print("Autumn")

elif (input_month == 'December' and input_day >= 21) or input_month == 'January' or input_month == 'February' or (
        input_month == 'March' and input_day <= 19):
    print("Winter")

else:
    print("Invalid")