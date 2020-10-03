# Luis Onate
# 1596900

def reverse(user_txt):  # reverse function definition
    return user_txt[::-1]  # slicing the user input to read backwards


user_input = input().strip()  # removing whitespace from start and end of user input
separate = user_input.split(' ')  # splitting user input into separate strings
build = ''.join(separate)  # joining split back together to have one string with no whitespace at all

if build == reverse(build):  # if-else statement checking if user input is read the same in reverse form
    print(user_input, 'is a palindrome')  # if read the same in reverse form, prints user_input is a palindrome
else:  # else if not read the same in reverse form, prints user_input is not a palindrome
    print(user_input, 'is not a palindrome')
