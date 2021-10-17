def check_character(word, index):
    for i, char in enumerate(word):
        if i == index:
            if char.islower() == True or char.isupper() == True:
                return ("Character '{}' is a letter".format(char))
            elif char.isspace() == True:
                return ("Character ' ' is a white space")
            elif char.isdigit() == True:
                return ("Character '{}' is a digit".format(char))
            else:
                return ("Character '{}' is unknown".format(char))
        else:
            continue

    # islower() or isupper()
    # isspace()
    # isdigit()
    # else unknown


if __name__ == '__main__':
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))