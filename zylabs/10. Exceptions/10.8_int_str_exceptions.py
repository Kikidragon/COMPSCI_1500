# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
      #Insert try/except blocks to catch the exception.
    try:
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))
    except:
        age = 0
        print('{} {}'.format(name, age))

    # Get next line
    parts = input().split()
    name = parts[0]