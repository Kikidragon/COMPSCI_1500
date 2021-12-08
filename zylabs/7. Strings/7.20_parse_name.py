inp = input("Enter input string:\n")
# inp = input("Enter input string:\n")
while inp != 'q':
    if ',' in inp:
        inp = inp.replace(' ', '')
        x = inp.split(',')
        a = x[0]
        b = x[1]

        print("First word: {}".format(a))
        print("Second word: {}".format(b))
        print()
    else:
        print("Error: No comma in string.")
        print()

    inp = input("Enter input string:\n")

