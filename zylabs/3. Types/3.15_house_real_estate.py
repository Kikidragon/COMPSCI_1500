current_price = int(input())
last_months_price = int(input())

change = current_price - last_months_price
mortgage = (current_price * 0.051) / 12

print("This house is ${0}. The change is ${1} since last month.".format(current_price, change))
print("The estimated monthly mortgage is ${:.2f}.".format(mortgage))
