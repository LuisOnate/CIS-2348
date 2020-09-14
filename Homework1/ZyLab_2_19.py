# Luis Onate
# 1596900

# assigns initial values to four variables
lemon_juice = 0
water = 0
agave_nectar = 0
serv = 0

# requests user for integer value representing cups of lemon juice
lemon_juice = int(input('Enter amount of lemon juice (in cups):\n'))

# request user for integer value representing cups of water
water = int(input('Enter amount of water (in cups):\n'))

# requests user for integer value representing cups of agave nectar
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))

# requests user for integer representing how many servings is made with said cups of each ingredient
serv1 = int(input('How many servings does this make?\n\n'))

# outputs the predetermined amounts of each ingredient for the base serving size
print('Lemonade ingredients - yields', '{:.2f}'.format(serv1), 'servings')
print('{:.2f}'.format(lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave_nectar), 'cup(s) agave nectar\n')

# request user with a wanted serving size
serv = int(input('How many servings would you like to make?\n\n'))

# outputs quantity of ingredients for the desired serving size requested above
print('Lemonade ingredients - yields', '{:.2f}'.format(serv), 'servings')
print('{:.2f}'.format(lemon_juice * serv / serv1), 'cup(s) lemon juice')
print('{:.2f}'.format(water * serv / serv1), 'cup(s) water')
print('{:.2f}'.format(agave_nectar * serv / serv1), 'cup(s) agave nectar\n')

# converts the amount of each ingredient from cups to gallons and displays it on screen
print('Lemonade ingredients - yields', '{:.2f}'.format(serv), 'servings')
print('{:.2f}'.format(((serv / serv1) * lemon_juice) / 16), 'gallon(s) lemon juice')
print('{:.2f}'.format(((serv / serv1) * water) / 16), 'gallon(s) water')
print('{:.2f}'.format(((serv / serv1) * agave_nectar) / 16), 'gallon(s) agave nectar')
