# Luis Onate
# 1596900

# imports math module
import math

# request user to input wall height followed by wall width
height = int(input('Enter wall height (feet):\n'))
width = int(input('Enter wall width (feet):\n'))

# wall area is calculated by multiplying height by width
wall_area = height * width
print('Wall area:', wall_area, 'square feet')  # wall area is outputted to screen

# area that can be covered by one can is assigned to variable gall1_covers
gall1_covers = 350
gallons_needed = wall_area / gall1_covers  # number of paint gallons needed is calculated
print('Paint needed:', '{:.2f}'.format(gallons_needed), 'gallons')  # gallons needed is displayed to screen

# gallons needed rounded up to next whole number and assigned to variable cans
cans = math.ceil(gallons_needed)
print('Cans needed:', cans, 'can(s)\n')  # cans needed outputted to display

# cost associated to color
costs = {'red': 35, 'blue': 25, 'green': 23}
color_pick = input('Choose a color to paint the wall:\n')

if color_pick == 'red':
    print('Cost of purchasing red paint: $', (costs['red'] * cans), sep="")
if color_pick == 'blue':
    print('Cost of purchasing blue paint: $', (costs['blue'] * cans), sep="")
if color_pick == 'green':
    print('Cost of purchasing green paint: $', (costs['green'] * cans), sep="")
