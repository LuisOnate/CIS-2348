# Luis Onate
# 1596900

# output of 'Birthday Calculator' and 'Current day' to display.
print('Birthday Calculator')
print('Current day')

# requests users for input of current day information, month, day, and year, accordingly.
current_month = int(input('Month: '))
current_day = int(input('Day: '))
current_year = int(input('Year: '))

# outputs 'Birthday to display.
print('Birthday')

# request users for birthday information, month, day, and year, accordingly.
birthday_month = int(input('Month: '))
birthday_day = int(input('Day: '))
birthday_year = int(input('Year: '))

# if statement and nested if statement displaying 'Happy Birthday!!!'--
# if current day and month are the same as birthday day and month.
if current_month == birthday_month:
    if current_day == birthday_day:
        print('Happy Birthday!!!')

age = current_year - birthday_year  # age calculated and assigned to variable 'age'.
if current_month >= birthday_month:  # if-else statement with nested if statement calculating age if--
    if current_day >= birthday_day:  # parameters return true values else age is replaced with age minus--
        age = current_year - birthday_year  # 1 to display the age before the arrival of birthday.
else:
    age = age - 1
print('You are', age, 'years old.')  # outputs the age of a person to the screen.
