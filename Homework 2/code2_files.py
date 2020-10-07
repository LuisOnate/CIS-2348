# Luis Onate
# 1596900

# open input file for reading and opening parsedDates.txt file to write onto
input_date = open(input(), 'r')
output_date = open('parsedDates.txt', 'w')
dates = input_date.readlines()

# list of months of the year
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

# for loop checking for true or false format
for string in dates:
    if string == '-1':  # for strings in the input file with -1, string is not written to parsedDates.txt file
        pass

    sep_str = string.split()  # strings are split into seperate strings
    num_str = len(sep_str)
    if num_str != 3:  # when split, if number of split strings isn't three, strings are not written to new file
        continue
    mon = sep_str[0]
    day = sep_str[1]
    years = sep_str[2]
    if day != day[0: 1]:  # For day to print without the comma in the string
        comma = day[-1]  # index of the comma
        if comma == ',':
            day = day[:len(day)-1]  # assigns day with range that excludes the comma

    for month in range(12):  # for loop iteration conditioning dates new output
        if string.find(months[month]) >= 0:  # if string in input file found in list, format month string to number
            mo = str(month + 1)  # month assigned number  in range 1-12
            formatted_date = mo + '/' + day + '/' + years  # format in which output is to be written to new file
            output_date.write(formatted_date)  # write output to new file
            output_date.write("\n")  # skip line in new file
            print(formatted_date)

# close input file and output file
input_date.close()
output_date.close()
