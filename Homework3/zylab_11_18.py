# Luis Onate
# 1596900

user_input = input()  # user requested input
nums = user_input.split()  # splits user input into separate strings

numbers = []  # creates empty list

for i in nums:  # outer loop converts strings to integers and appends them to the numbers list
    numbers.append(int(i))
    for num in numbers:  # inner look checks for negative numbers and removes them from list
        if num < 0:
            numbers.remove(num)
    numbers.sort()  # sorts the list in ascending order
for num in numbers:  # loop iteration that prints out all the numbers in the list
    print(num, end=' ')
