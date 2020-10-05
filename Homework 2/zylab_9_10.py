# Luis Onate
# 1596900

# csv module import
import csv

# user input of a file
input1_csv = input()

# creating an empty dictionary to store the words and their frequencies
display_word_times = {}

# opening the file with the csv.reader() method
with open(input1_csv, 'r') as csvfile:
    file = csv.reader(csvfile)
    # for and while loop counting the instances of the words and adding them to the dictionary
    for row in file:
        for word in row:
            while word not in display_word_times.keys():
                display_word_times[word] = 0
                continue
            while word in display_word_times.keys():
                display_word_times[word] += 1
                break
# for loop printing all words and the value of the times they appear
for word in display_word_times.keys():
    print(word, str(display_word_times[word]))
