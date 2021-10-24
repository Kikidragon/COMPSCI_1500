def get_user_values():
    numint = int(input())
    my_list = []
    while numint > 0:
        numint -= 1
        value = int(input())
        my_list.append(value)
    upper_threshold = int(input())
    return my_list, upper_threshold

def output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    for i in user_values:
        if i <= upper_threshold:
            print(i)
        else:
            continue

if __name__ == '__main__':
    user_values, upper_threshold = get_user_values()
    output_ints_less_than_or_equal_to_threshold(user_values, upper_threshold)
    # print(upper_threshold)
