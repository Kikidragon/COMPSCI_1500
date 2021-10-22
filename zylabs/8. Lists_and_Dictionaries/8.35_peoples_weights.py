weights = []
w1 = float(input("Enter weight 1:\n"))
weights.append(w1)
w2 = float(input("Enter weight 2:\n"))
weights.append(w2)
w3 = float(input("Enter weight 3:\n"))
weights.append(w3)
w4 = float(input("Enter weight 4:\n"))
weights.append(w4)
print("Weights: {}".format(weights))
print()
#average
x=0
for i in weights:
    x += i
avg = x / len(weights)
print("Average weight: {:.2f}".format(avg))
print("Max weight: {:.2f}".format(max(weights)))
print()
#index and weight (lb, kg)
loc = int(input("Enter a list location (1 - 4):\n"))
loc -=1
y = weights[loc]
print("Weight in pounds: {:.2f}".format(y))
kg = y / 2.2
print("Weight in kilograms: {:.2f}".format(kg))
print()
#sort list
print("Sorted list: {}".format(sorted(weights)))



