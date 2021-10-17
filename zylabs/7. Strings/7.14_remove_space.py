def remove_spaces(user_string):
    return user_string.replace(' ', '')

    # no_space = []
    # for c in user_string:
    #     if c.isspace() == False:
    #         no_space.append(c)
    #     else:
    #         continue
    # for i in no_space:
    #     print(i, end='')

if __name__ == '__main__':
    words = input()
    print(remove_spaces(words))
