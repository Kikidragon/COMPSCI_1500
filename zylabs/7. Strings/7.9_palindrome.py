word = input()
worda = word.replace(' ', '')
word2 = worda[::-1]
# print(word2)
if worda == word2:
    print('{} is a palindrome'.format(word))
else:
    print('{} is not a palindrome'.format(word))
