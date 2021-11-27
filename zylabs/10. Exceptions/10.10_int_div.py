user_num = input()
div_num = input()
#output user_num / div_num
try:
    if user_num == float:
        raise ValueError
    elif div_num == float:
        raise ValueError
    else:
        x = int(user_num) / int(div_num)
        print('{:.0f}'.format(x))
except ZeroDivisionError:
    print("Zero Division Exception: integer division or modulo by zero")
except ValueError as e:
    print("Input Exception: {}".format(e))
# except Exception as e:
#     print("Input Exception: invalid literal for int() with base 10. Exceptions: {}".format(e))
