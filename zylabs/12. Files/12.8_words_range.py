text = input()
start = input()
end = input()
f = open(text)
file = f.readlines()
for word in file:
    word = word.strip()
    if start <= word <= end:
        print(word)
f.close()
