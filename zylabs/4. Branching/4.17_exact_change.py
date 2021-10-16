total_change = int(input())
import math
# Quarter 25, Dime 10, Nickel 5, Penny 1
Dollars = total_change / 100
Quarters = (total_change % 100) / 25
Dimes = ((total_change % 100) %25) / 10
Nickels = (((total_change % 100) % 25) % 10) / 5
Pennies = ((((total_change % 100) % 25) % 10) % 5)
Do = math.floor(Dollars)
Q = math.floor(Quarters)
D = math.floor(Dimes)
N = math.floor(Nickels)
P = math.floor(Pennies)

if Do == 1:
    print(Do, "Dollar")
elif 1 < Do:
    print(Do, "Dollars")

if Q == 1:
    print(Q, "Quarter")
elif 1 < Q:
    print(Q, "Quarters")

if D == 1:
    print(D, "Dime")
elif 1 < D:
    print(D, "Dimes")

if N == 1:
    print(N, "Nickel")
elif 1 < N:
    print(N, "Nickels")

if P == 1:
    print(P, "Penny")
elif 1 < P:
    print(P, "Pennies")

if total_change <= 0:
    print("No change")