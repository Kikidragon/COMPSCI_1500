# FIXME UNFINISHED

def a(roster):
    jer1 = int(input("Enter a new player's jersey number:\n"))
    rat1 = int(input("Enter a new player's rating:\n"))
    pl1 = {jer1: rat1}
    roster.update(pl1)


def d(roster):
    pass
    jer1 = int(input("Enter a jersey number:\n"))
    for i in range(len(roster)):
        if jer1 in roster[i]:
            del roster[i]
    # for player in roster:
    #     if jer1 in player:
    #         roster.remove(player)

    # for player in roster:
    #     for key, val in player.items():
    #         if key == jer1:
    #             roster.remove(player)
# FIXME


def u(roster):
    pass
    jer1 = int(input("Enter a jersey number:\n"))
    rat1 = int(input("Enter a new rating for player:\n"))
    pl1 = {jer1: rat1}
    # FIXME REMOVE ORIGINAL PLAYER
    roster.update(pl1)


def r(roster):
    pass


def o(roster):
    ros_sort = {}
    for i in sorted(roster):
        ros_sort[i] = roster[i]
    print("ROSTER")
    for jer, rat in ros_sort.items():
        print("Jersey number: {}, Rating: {}".format(jer, rat))
    print()


def print_menu():
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()


def execute_menu(choice, roster):
    if choice == 'a':
        return a(roster)
    if choice == 'd':
        return d(roster)
    if choice == 'u':
        return u(roster)
    if choice == 'r':
        return r(roster)
    if choice == 'o':
        return o(roster)
    return choice


if __name__ == '__main__':

    #5 inputs
    roster = {}
    jer1 = int(input("Enter player 1's jersey number:\n"))
    rat1 = int(input("Enter player 1's rating:\n"))
    pl1 = {jer1 : rat1}
    roster.update(pl1)
    print()
    jer2 = int(input("Enter player 2's jersey number:\n"))
    rat2 = int(input("Enter player 2's rating:\n"))
    pl2 = {jer2 : rat2}
    roster.update(pl2)
    print()
    jer3 = int(input("Enter player 3's jersey number:\n"))
    rat3 = int(input("Enter player 3's rating:\n"))
    pl3 = {jer3 : rat3}
    roster.update(pl3)
    print()
    jer4 = int(input("Enter player 4's jersey number:\n"))
    rat4 = int(input("Enter player 4's rating:\n"))
    pl4 = {jer4 : rat4}
    roster.update(pl4)
    print()
    jer5 = int(input("Enter player 5's jersey number:\n"))
    rat5 = int(input("Enter player 5's rating:\n"))
    pl5 = {jer5 : rat5}
    roster.update(pl5)
    print()
    #print roster list sorted by jersey number
    ros_sort = {}
    for i in sorted(roster):
        ros_sort[i] = roster[i]
    print("ROSTER")
    for jer, rat in ros_sort.items():
        print("Jersey number: {}, Rating: {}".format(jer, rat))
    print()
    #print menu
    print_menu()
    choice = input("Choose an option:\n")
    if choice == 'a' or choice == 'd' or choice == 'u' or choice == 'r' or choice == 'o':
        execute_menu(choice, roster)
    else:
        while choice != 'q':
            print_menu()
            print()
            choice = input("Choose an option:")
            if choice == 'a' or choice == 'd' or choice == 'u' or choice == 'r' or choice == 's\o':
                execute_menu(choice, roster)
