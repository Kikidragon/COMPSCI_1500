services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()

if service_choice1 == 'Air freshener':
    serv1 = services['Air freshener']
elif service_choice1 == 'Rain repellent':
    serv1 = services['Rain repellent']
elif service_choice1 == 'Tire shine':
    serv1 = services['Tire shine']
elif service_choice1 == 'Wax':
    serv1 = services['Wax']
elif service_choice1 == 'Vacuum':
    serv1 = services['Vacuum']
else:
    serv1 = 0

if service_choice2 == 'Air freshener':
    serv2 = services['Air freshener']
elif service_choice2 == 'Rain repellent':
    serv2 = services['Rain repellent']
elif service_choice2 == 'Tire shine':
    serv2 = services['Tire Shine']
elif service_choice2 == 'Wax':
    serv2 = services['Wax']
elif service_choice2 == 'Vacuum':
    serv2 = services['Vacuum']
else:
    serv2 = 0

total = base_wash + serv1 + serv2
if service_choice1 == '-' and service_choice2 == '-':
    print("ZyCar Wash")
    print("Base car wash -- ${}".format(base_wash))
    print("----")
    print("Total price: ${}".format(total))
elif service_choice1 == '-':
    print("ZyCar Wash")
    print("Base car wash -- ${}".format(base_wash))
    print("{} -- ${}".format(service_choice2, serv2))
    print("----")
    print("Total price: ${}".format(total))
elif service_choice2 == '-':
    print("ZyCar Wash")
    print("Base car wash -- ${}".format(base_wash))
    print("{} -- ${}".format(service_choice1, serv1))
    print("----")
    print("Total price: ${}".format(total))
else:
    print("ZyCar Wash")
    print("Base car wash -- ${}".format(base_wash))
    print("{} -- ${}".format(service_choice1, serv1))
    print("{} -- ${}".format(service_choice2, serv2))
    print("----")
    print("Total price: ${}".format(total))

# if first == "Oil change":
#     serv1 = services["Oil change"]
# elif first == "Tire rotation":
#     serv1 = services["Tire rotation"]
# elif first == "Car wash":
#     serv1 = services["Car wash"]
# elif first == "Car wax":
#     serv1 = services["Car wax"]
# else:
#     serv1 = 0

# if second == "Oil change":
#     serv2 = services["Oil change"]
# elif second == "Tire rotation":
#     serv2 = services["Tire rotation"]
# elif second == "Car wash":
#     serv2 = services["Car wash"]
# elif second == "Car wax":
#     serv2 = services["Car wax"]
# else:
#     serv2 = 0

# print()
# print("Davy's auto shop invoice")
# print()
# if first == "-":
#     print("Service 1: No service")
#     print("Service 2: " + second + ", ${:.0f}".format(serv2))
# elif second == "-":
#     print("Service 1: " + first + ", ${:.0f}".format(serv1))
#     print("Service 2: No service")
# else:
#     print("Service 1: " + first + ", ${:.0f}".format(serv1))
#     print("Service 2: " + second + ", ${:.0f}".format(serv2))
# print()
# print("Total: ${:.0f}".format(serv1 + serv2))
# #choice 1
# #choice 2
