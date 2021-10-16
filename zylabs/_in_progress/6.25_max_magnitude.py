import math
#FIXME UNFINISHED
def max_magnitude(user_val1, user_val2):
    list1 = []
    if user_val1 < 0 or user_val2 < 0:
        if user_val1 < 0:
            x = user_val1 * -1
            list1.append(x)
        if user_val2 < 0:
            y = user_val2 * -1
            list1.append(y)
        else:
            x = user_val1
            y = user_val2
            list1.append(y)
            list1.append(x)
        if max(list1) == x:
            return user_val1
        elif max(list1) == y:
            return user_val2
    else:
        list1.append(user_val1)
        list1.append(user_val2)
        return max(list1)