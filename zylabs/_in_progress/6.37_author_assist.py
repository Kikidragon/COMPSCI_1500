def print_menu():
    # prints the menu
    print('MENU')
    print('c - Number of non-whitespace characters')
    print('w - Number of words')
    print('f - Fix capitalization')
    print('r - Replace punctuation')
    print('s - Shorten spaces')
    print('q - Quit')
    # redirects to the proper choice

#FIXME implement q

def get_num_of_non_WS_characters(text):
    count = 0
    for c in text:
        if c != ' ':
            count += 1
        else:
            continue
    return count
    # WORKS fully complete
    # c - Number of non-whitespace characters


def get_num_of_words(text):
    words = text.split()
    for i in words:
        i = i.strip
    word = ' '.join(words)
    words2 = word.split()
    # word_real = []
    # for i in words:
    #     if type(i) == str:
    #         word_real.append(i)
    num = len(words2)
    return num
    # FIXME so it returns only words not just anything separated by a space
    # WORKS has output
    # w - Number of words


def fix_capitalization(text):
    sent = text.split('.')
    for i in sent:
        i = i.capitalize()
    sent2 = '.'.join(sent)
    print("Edited text:", sent2)
    # f - Fix capitalization
    # FIXME do this one



def replace_punctuation(text):
    count_exc = 0
    count_semi = 0
    for i in text:
        if i == '!':
            count_exc += 1
        elif i == ';':
            count_semi += 1
    text = text.replace('!', '.')
    text = text.replace(';', ',')
    return count_exc, count_semi, text
    # print("exclamation_count:", count_exc)
    # print("semicolon_count:", count_semi)
    # print("Edited text:", text)
    #WORKS FULLY
    # return count_exc, count_semi, text
    # WORKS
    # r - Replace punctuation


def shorten_space(text):
    words = text.split()
    for i in words:
        i = i.strip
    word = ' '.join(words)
    return word
    # print("Edited text:", word)
    # text = text.replace('  ', ' ')
    # return text
    # s - Shorten spaces
    # WORKS FULLY


def execute_menu(choice, text):
    if choice == 'c':
        return "Number of non-whitespace characters: ", get_num_of_non_WS_characters(text)
    elif choice == 'w':
        return "Number of words: ", get_num_of_words(text)
    elif choice == 'f':
        return "Edited text: ", fix_capitalization(text)
    elif choice == 'r':
        exc, semi, txt = replace_punctuation(text)
        return "exclamation_count: {}\nsemicolon_count: {}\nEdited text: {}".format(exc, semi, txt)
    elif choice == 's':
        return "Edited text: ", shorten_space(text)
    elif choice == 'q':
        return -1


if __name__ == '__main__':
    phrase = input("Enter a sample text:\n")
    print()
    print("You entered: {}".format(phrase))
    print()
    print_menu()
    print()
    choice = input("Choose an option:\n")
    # execute_menu(choice, phrase)
    while choice != 'q':
        if choice == 'c' or choice == 'w' or choice == 'f' or choice == 'r' or choice == 's':
            for i in execute_menu(choice, phrase):
                print(i, end='')
            print()
            print()
            print_menu()
            print()
            choice = input("Choose an option:\n")
        else:
            while choice != 'q':
                print()
                print_menu()
                print()
                choice = input("Choose an option:\n")
                print()
                if choice == 'c' or choice == 'w' or choice == 'f' or choice == 'r' or choice == 's':
                    for i in execute_menu(choice, phrase):
                        print(i,end='')
                    print()

#FIXME make them all return statements not print statements