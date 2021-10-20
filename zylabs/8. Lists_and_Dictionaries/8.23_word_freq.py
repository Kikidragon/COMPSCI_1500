word = input()
words = word.split()
freq = []

for word in words:
    x = words.count(word)
    print(word, x)

# for i in words:
#     freq.append(words.count(i))

# for i in words:
#     for x in freq:
#         print(i, x)

# for word in text:
#         freq = text.count(word)
#         print(word, freq)


# wordfreq = []
# for w in wordlist:
#     wordfreq.append(wordlist.count(w))


# Find()/rfind() -> hello.find(x) returns lowest index x in hello  (rfind greatest index)


# the_word = input()
# x = the_word.split()
# check = x.pop(0)
# count = 0
# for y in x:
#     if y == check:
#         count += 1
#     else:
#         continue
# print(count)

