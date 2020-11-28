# Luis Onate
# 1596900

# selection sorting algorithm
def selection_sort_descend_trace(lis):
    for i in range(len(lis) - 1):
        index_largest = i  # for loop assigns the variable index_largest with index i
        for j in range(i + 1, len(lis)):
            if lis[j] > lis[index_largest]:  # for loop used for assigning the variable, index_largest, with index j if
                index_largest = j  # index i is smaller than index j


        temp = lis[i]
        lis[i] = lis[index_largest]
        lis[index_largest] = temp
        for num in lis:  # for loop used for printing out the list after every iteration
            print(int(num), end=' ')
        print()


if __name__ == "__main__":
    user_input = input()  # take in user input
    my_list = user_input.split()  # create list with user input
    my_list2 = [int(num) for num in my_list]  # convert the strings in the list into integers

    # call to selection_sort_descend_trace function with the list created as the parameter
    selection_sort_descend_trace(my_list2)
