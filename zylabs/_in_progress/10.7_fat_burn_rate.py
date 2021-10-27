def get_age():
    age = int(input())
    valid = False
    while not valid:
        try:
            if age <= 18 or age >= 75:
                raise ValueError
            else:
                valid = True
        except ValueError:
            print("Invalid age.")
            print("Could not calculate heart rate info.\n")
            break
    # TODO: Raise excpetion for invalid ages
    return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = .7* (220 - age)
    return heart_rate

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    age = get_age()
    if age >= 18 and age <= 75:
        print("Fat burning heart rate for a {} year-old: {} bpm".format(age, fat_burning_heart_rate(age)))