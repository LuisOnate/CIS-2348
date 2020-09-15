# Luis Onate
# 1596900

# initial output of Davy's automotive menue
print(
    "Davy's auto shop services\n"
    "Oil change -- $35\n"
    "Tire rotation -- $19\n"
    "Car wash -- $7\n"
    "Car wax -- $12\n"
)

# cost dictionary associated with service prices
cost = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0}

# requests user to select two services
service1 = input('Select first service:\n')
service2 = input('Select second service:\n\n')

# if else statements that print selected service 1 to display
print("Davy's auto shop invoice\n")
if service1 == 'Oil change':
    print('Service 1: Oil change, $35')
elif service1 == 'Tire rotation':
    print('Service 1: Tire rotation, $19')
elif service1 == 'Car wash':
    print('Service 1: Car wash, $7')
elif service1 == 'Car wax':
    print('Service 1: Car wax, $12')
else:
    print('Service 1: No service')

# if else statement that print selected service 2 to display
if service2 == 'Oil change':
    print('Service 2: Oil change, $35\n')
elif service2 == 'Tire rotation':
    print('Service 2: Tire rotation, $19\n')
elif service2 == 'Car wash':
    print('Service 2: Car wash, $7\n')
elif service2 == 'Car wax':
    print('Service 2: Car wax, $12\n')
else:
    print('Service 2: No service\n')

# cost of service calculated and assigned to variable
total = cost[service1] + cost[service2]
print('Total: $', total, sep="")  # output of cost to screen
