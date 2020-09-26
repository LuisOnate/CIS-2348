# Luis Onate
# 1596900

# request user input for function 1
user_x1 = int(input())
user_y1 = int(input())
user_total1 = int(input())

# request user input for function 2
user_x2 = int(input())
user_y2 = int(input())
user_total2 = int(input())

# brute force for loop testing values for x and y in range -10 through 10
solution = 0
for x in range(-10, 11):
    for y in range(-10, 11):
        while ((user_x1 * x) + (user_y1 * y) == user_total1) and ((user_x2 * x) + (user_y2 * y) == user_total2):
            solution = 1  # while the x and y values satisfy equation solution is assigned with value 1
            if solution:  # when solution is assigned with 1, values of x and y print to screen
                print(x, y)
                break
if not solution:  # if solution doesn't have a value of 1 assigned to it, 'No solution' prints to screen
    print('No solution')
