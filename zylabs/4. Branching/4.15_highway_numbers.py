highway_number = int(input())

if 1 <= highway_number <= 99:
    if highway_number % 2 == 0:
        print("I-{:.0f} is primary, going east/west.".format(highway_number))
    else:
        print("I-{:.0f} is primary, going north/south.".format(highway_number))
elif highway_number == 200:
    print(highway_number, "is not a valid interstate highway number.")
elif 100 <= highway_number <= 999:
    main = highway_number % 100
    if main % 2 == 0:
        print("I-{:.0f} is auxiliary, serving I-{:.0f}, going east/west.".format(highway_number, main))
    else:
        print("I-{:.0f} is auxiliary, serving I-{:.0f}, going north/south.".format(highway_number, main))
else:
    print(highway_number, "is not a valid interstate highway number.")