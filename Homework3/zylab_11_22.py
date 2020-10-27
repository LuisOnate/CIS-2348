# Luis Onate
# 1596900

user_input = input()  # request user input
word_strings = user_input.split()  # separates user inputted string into multiple strings at space between each string

words = []  # creates empty list

for word in word_strings:  # for-loop that appends the words in the split string into the empty list
    words.append(word)

word_frequency = {word: 0 for word in words}  # creates dictionary using the words list

for word in words:  # for-loop increasing the frequency of the value of the keys in the dictionary if they repeat
    if word in word_frequency:
        word_frequency[word] += 1

for word in words:  # for-loop that prints the words in the list with the frequency they appear with in the dictionary
    print(word, word_frequency[word])
