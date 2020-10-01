# Luis Onate
# 1596900

# function definition for exact_change
def exact_change(user_total):
    if user_total <= 0:  # if statement checking the value of user_total and if less than 0-
        print("no change")  # 'no change' is displayed to screen
    # else, user_total larger than 0, a series of if-else statements are tested
    else:
        dollars = user_total // 100  # dollars is assigned with largest whole number that can be taken from user_total
        user_total = user_total % 100  # user_total is reassigned with modulo of 100
        if dollars == 0:  # if value is 0 for dollars, quarters, dimes, nickels,-
            pass  # and pennies, the value isn't displayed
        elif 1 <= dollars < 2:
            print(dollars, "dollar")
        else:
            print(dollars, "dollars")

        quarters = user_total // 25  # quarters is assigned with largest whole number that can be taken from user_total
        user_total = user_total % 25  # user_total is reassigned with modulo of 25
        if quarters == 0:
            pass
        elif 1 <= quarters < 2:
            print(quarters, "quarter")
        else:
            print(quarters, "quarters")

        dimes = user_total // 10  # dimes is assigned with largest whole number that can be taken from user_total
        user_total = user_total % 10  # user_total is reassigned with modulo of 10
        if dimes == 0:
            pass
        elif 1 <= dimes < 2:
            print(dimes, "dime")
        else:
            print(dimes, "dimes")

        nickels = user_total // 5  # nickels is assigned with largest whole number that can be taken from user_total
        user_total = user_total % 5  # user_total is reassigned with modulo of 5
        if nickels == 0:
            pass
        elif 1 <= nickels < 2:
            print(nickels, "nickel")
        else:
            print(nickels, "nickels")

        pennies = user_total // 1  # pennies is assigned with largest whole number that can be taken from user_total
        if pennies == 0:
            pass
        elif 1 <= pennies < 2:  # if only 1 for any of the five money types, the description is singular
            print(pennies, "penny")
        else:
            print(pennies, "pennies")  # if more than 1 for any of the five money types, the description is plural
        return dollars, quarters, dimes, nickels, pennies


if __name__ == '__main__':  # unit testing
    total_money_to_exact_change = int(input())  # user requested input
    exact_change(total_money_to_exact_change)  # function is called
