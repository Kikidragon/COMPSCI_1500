# Type your code here
services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12}
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()
first = input("Select first service:\n")
second = input("Select second service:\n")
if first == "Oil change":
    serv1 = services["Oil change"]
elif first == "Tire rotation":
    serv1 = services["Tire rotation"]
elif first == "Car wash":
    serv1 = services["Car wash"]
elif first == "Car wax":
    serv1 = services["Car wax"]
else:
    serv1 = 0

if second == "Oil change":
    serv2 = services["Oil change"]
elif second == "Tire rotation":
    serv2 = services["Tire rotation"]
elif second == "Car wash":
    serv2 = services["Car wash"]
elif second == "Car wax":
    serv2 = services["Car wax"]
else:
    serv2 = 0

print()
print("Davy's auto shop invoice")
print()
if first == "-":
    print("Service 1: No service")
    print("Service 2: " + second + ", ${:.0f}".format(serv2))
elif second == "-":
    print("Service 1: " + first + ", ${:.0f}".format(serv1))
    print("Service 2: No service")
else:
    print("Service 1: " + first + ", ${:.0f}".format(serv1))
    print("Service 2: " + second + ", ${:.0f}".format(serv2))
print()
print("Total: ${:.0f}".format(serv1 + serv2))