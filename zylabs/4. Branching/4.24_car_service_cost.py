#Oil change -- $35
#Tire rotation -- $19
#Car wash -- $7'''
service = input("Enter desired auto service:\n")
print("You entered:", service)

if service == 'Oil change':
    print("Cost of oil change: $35")
elif service == 'Tire rotation':
    print("Cost of tire rotation: $19")
elif service == 'Car wash':
    print("Cost of car wash: $7")
else:
    print("Error: Requested service is not recognized")