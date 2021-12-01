# def get_age():
#     age = int(input())
#     valid = False
#     while not valid:
#         try:
#             if age <= 18 or age >= 75:
#                 raise ValueError
#             else:
#                 valid = True
#         except ValueError:
#             print("Invalid age.")
#             print("Could not calculate heart rate info.\n")
#             break
#     return age
#
# def fat_burning_heart_rate(age):
#     heart_rate = .7* (220 - age)
#     return heart_rate
#
# if __name__ == "__main__":
#     age = get_age()
#     if age >= 18 and age <= 75:
#         print("Fat burning heart rate for a {} year-old: {} bpm".format(age, fat_burning_heart_rate(age)))

def get_age():
    age = int(input())
    if 18 <= age <= 75:
        return age
    raise ValueError("Invalid age.")


def fat_burning_heart_rate(age):
    return (220 - age) * 0.7


if __name__ == "__main__":
    try:
        age = get_age()
        print("Fat burning heart rate for a {} year-old: {} bpm".format(age, fat_burning_heart_rate(age)))
    except ValueError as e:
        print(e)
        print("Could not calculate heart rate info.")
