def miles_to_laps(user_miles):
    laps = user_miles * 4
    return laps


if __name__ == '__main__':
    user_miles = float(input())
    print('{:.2f}'.format(miles_to_laps(user_miles)))
