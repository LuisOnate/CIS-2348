# Luis Onate
# 1596900

# user input assigned to variable user_password
user_password = input()
password = ''  # empty string assigned to variable password

# for loop that replaces characters 'i, a, m, B, and o' with '!, @, M, 8, and .' respectively
for character in user_password:
    if character == 'i':
        password += '!'
    elif character == 'a':
        password += '@'
    elif character == 'm':
        password += 'M'
    elif character == 'B':
        password += '8'
    elif character == 'o':
        password += '.'
    else:
        password += character

# for loop that adds the string 'q*s' to the end of the string assigned to password and breaks after on loop
for character in user_password:
    password += 'q*s'
    break

# prints the string assigned to password
print(password)
