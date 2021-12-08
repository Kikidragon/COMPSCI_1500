# not done correctly
import itertools
def all_permutations(permList, nameList):
    # count = math.factorial(len(nameList)) # number of answers
    # while count != 0:
    #     pass
    #
    # if len(nameList) == 1:
    #     print(nameList[0])
    # else:
    #     for x in nameList:
    #         nameList.remove(x)
    #         y = all_permutations(permList, nameList)
    #         permList.append(y)
    #         print(permList)


    perm = list(itertools.permutations(nameList))
    for i in perm:
        for j in i:
            print(j, end=' ')
        print()

#https://stackoverflow.com/questions/33312532/generate-all-permutations-of-a-string-in-python-without-using-itertools

            # all_permutations(nameList[:i] + nameList[i+1:], permList+nameList[i:i+1])


    # if nameList + 1 >= len(permList):
    #     return permList
    # else:
    #     for p in all_permutations(permList, nameList+1):
    #         print(p)
    #     for i in range(nameList + 1, len(permList)):
    #         permList[nameList]

    # if len(nameList) == 0:
    #     return []
    # if len(nameList) == 1:
    #     return [nameList]
    # for i in range(len(nameList)):
    #     x = nameList[i]
    #     remaining = nameList[:i] + nameList[i+1:]
    #     for j in all_permutations(remaining, nameList):
    #         permList.append([x]+j)
    #     return permList

    # if len(permList) == 0:
    #     print(nameList)
    # else:
    #     for i in range(len(permList)):
    #         words = permList[i]
    #         remaining = permList[:i] + permList[i+1:]
    #         all_permutations(remaining, nameList+words)


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