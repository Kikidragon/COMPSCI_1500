# The words parameter is a list of strings.
def build_dictionary(words):
    # The frequencies dictionary will be built with your code below.
    # Each key is a word string and the corresponding value is an integer
    # indicating that word's frequency.
    dict1 = {}
    for word in words:
        x = words.count(word)
        case = {word: x}
        dict1.update(case)
        # dict1.append(word, x)
    return dict1

    # for entry in entries_list:
    # case = {'key1': entry[0], 'key2': entry[1], 'key3':entry[2] }
    # case_list.append(case)


# The following code asks for input, splits the input into a word list,
# calls build_dictionary(), and displays the contents sorted by key.
if __name__ == '__main__':
    words = input().split()
    your_dictionary = build_dictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(key + ': ' + str(your_dictionary[key]))

# word = input()
# words = word.split()
# freq = []

# for word in words:
#     x = words.count(word)
#     print(word, x)