# Luis Onate
# 1596900

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    # FIXME: The following line will throw ValueError exception.
    #        Insert try/except blocks to catch the exception.
    try:  # the try block increments the age by 1 of all inputs whose second index is an integer
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))

        # Get next line
        parts = input().split()
        name = parts[0]

    except ValueError:  # the except block checks to see if the second index in the user input is an integer and if not
        age = 0         # the value of the second index is changed to 0
        print('{} {}'.format(name, age))

        # Get next line
        parts = input().split()
        name = parts[0]
