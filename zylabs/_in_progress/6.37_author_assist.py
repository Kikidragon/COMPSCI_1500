def print_menu():
    # prints the menu
    print('MENU')
    print('c - Number of non-whitespace characters')
    print('w - Number of words')
    print('f - Fix capitalization')
    print('r - Replace punctuation')
    print('s - Shorten spaces')
    print('q - Quit')


def execute_menu(choice, text):
    # redirects to the proper choice
    def menu_c():
        # c - Number of non-whitespace characters
        pass

    def menu_w():
        # w - Number of words
        pass

    def menu_f():
        # f - Fix capitalization
        pass

    def menu_r():
        # r - Replace punctuation
        pass

    def menu_s():
        # s - Shorten spaces
        pass

    def menu_q():
        # q - Quit`
        pass


if __name__ == '__main__':
    phrase = input("Enter a sample text:\n")
    print()
    print("You entered: {}".format(phrase))
    print()
    print_menu()
    print()
    choice = input("Choose an option:")
    if choice == 'c' or choice == 'w' or choice == 'f' or choice == 'r' or choice == 's':
        execute_menu(choice, phrase)
    else:
        while choice != 'q':
            print_menu()
            print()
            choice = input("Choose an option:")
            if choice == 'c' or choice == 'w' or choice == 'f' or choice == 'r' or choice == 's':
                execute_menu(choice, phrase)