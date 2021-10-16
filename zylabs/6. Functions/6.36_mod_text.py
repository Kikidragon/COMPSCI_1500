def get_num_of_characters(input_str):
    c = 0
    for i in input_str:
        c += 1
    return c

def output_without_whitespace(input_str):
    str2 = input_str.replace(' ', '')
    return str2

if __name__ == '__main__':
    phrase = input("Enter a sentence or phrase:\n")
    print()
    print("You entered: {}".format(phrase))
    print()
    print("Number of characters: {}".format(get_num_of_characters(phrase)))
    print("String with no whitespace: {}".format(output_without_whitespace(phrase)))