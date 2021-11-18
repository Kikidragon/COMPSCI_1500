# FIXME UNFINISHED
def all_permutations(permList, nameList):
    if len(permList) == 0:
        print(nameList)
    else:
        for i in range(len(permList)):
            words = permList[i]
            remaining = permList[:i] + permList[i+1:]

    # TODO: Implement method to create and output all permutations of the list of names.

if __name__ == "__main__":
    nameList = input().split(' ')
    permList = []
    all_permutations(permList, nameList)

    # 14.6.1
    # def scramble(r_letters, s_letters):
    #     if len(r_letters) == 0:
    #         print(s_letters)
    #     else:
    #         for i in range(len(r_letters)):
    #             scramble_letter = r_letters[i]
    #             remaining_letters = r_letters[:i] + r_letters[i + 1:]
    #             scramble(remaining_letters, s_letters + scramble_letter)
    #
    #
    # word = input('Enter a word to be scrambled: ')
    # scramble(word, '')