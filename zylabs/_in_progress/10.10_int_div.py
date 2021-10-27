# Type your code here.
user_num = int(input())
div_num = int(input())
#output user_num / div_num
try:
    print(user_num / div_num)
except ZeroDivisionError:
    print("Zero Division Exception: integer division or modulo by zero")
except ValueError as e:
    print("Input Exception: invalid literal for int() with base 10: {}".format(e))