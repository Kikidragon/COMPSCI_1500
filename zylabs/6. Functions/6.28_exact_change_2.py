import math


def exact_change(user_total):
    total_change = user_total
    Dollars = total_change / 100
    Quarters = (total_change % 100) / 25
    Dimes = ((total_change % 100) % 25) / 10
    Nickels = (((total_change % 100) % 25) % 10) / 5
    Pennies = ((((total_change % 100) % 25) % 10) % 5)
    num_dollars = math.floor(Dollars)
    num_quarters = math.floor(Quarters)
    num_dimes = math.floor(Dimes)
    num_nickels = math.floor(Nickels)
    num_pennies = math.floor(Pennies)
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if num_dollars == 1:
        print(num_dollars, "dollar")
    elif 1 < num_dollars:
        print(num_dollars, "dollars")

    if num_quarters == 1:
        print(num_quarters, "quarter")
    elif 1 < num_quarters:
        print(num_quarters, "quarters")

    if num_dimes == 1:
        print(num_dimes, "dime")
    elif 1 < num_dimes:
        print(num_dimes, "dimes")

    if num_nickels == 1:
        print(num_nickels, "nickel")
    elif 1 < num_nickels:
        print(num_nickels, "nickels")

    if num_pennies == 1:
        print(num_pennies, "penny")
    elif 1 < num_pennies:
        print(num_pennies, "pennies")

    if input_val <= 0:
        print("no change")

# Dollars = total_change / 100
# Quarters = (total_change % 100) / 25
# Dimes = ((total_change % 100) %25) / 10. Exceptions
# Nickels = (((total_change % 100) % 25) % 10. Exceptions) / 5
# Pennies = ((((total_change % 100) % 25) % 10. Exceptions) % 5)
# Do = math.floor(Dollars)
# Q = math.floor(Quarters)
# D = math.floor(Dimes)
# N = math.floor(Nickels)
# P = math.floor(Pennies)

# if Do == 1:
#     print(Do, "Dollar")
# elif 1 < Do:
#     print(Do, "Dollars")

# if Q == 1:
#     print(Q, "Quarter")
# elif 1 < Q:
#     print(Q, "Quarters")

# if D == 1:
#     print(D, "Dime")
# elif 1 < D:
#     print(D, "Dimes")

# if N == 1:
#     print(N, "Nickel")
# elif 1 < N:
#     print(N, "Nickels")

# if P == 1:
#     print(P, "Penny")
# elif 1 < P:
#     print(P, "Pennies")

# if total_change <= 0:
#     print("No change")