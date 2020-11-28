# Luis Onate
# 1596900

# Global variable
num_calls = 0

# TODO: Write the partitioning algorithm - pick the middle element as the
#  pivot, compare the values using two index variables l and h (low and high),
#  initialized to the left and right sides of the current elements being sorted,
#  and determine if a swap is necessary


# partitioning algorithm
def partition(user_ids, i, k):
    # Selects the middle element as the pivot
    midpoint = i + (k - i) // 2  # midpoint calculated
    pivot = user_ids[midpoint]  # pivot assigned with midpoint of user_ids list

    done = False
    l = i  # variable l initialized
    h = k  # variable h initialized
    while not done:
        #  Increment l while numbers[l] < pivot
        while user_ids[l] < pivot:
            l = l + 1
        #  Decrement h while pivot < numbers[h]
        while pivot < user_ids[h]:
            h = h - 1
        if l >= h:
            done = True
        else:
            temp = user_ids[l]
            user_ids[l] = user_ids[h]
            user_ids[h] = temp
            l = l + 1
            h = h - 1
    return h


# TODO: Write the quicksort algorithm that recursively sorts the low and
#  high partitions. Add 1 to num_calls each time quisksort() is called


# quicksort algorithm
def quicksort(user_ids, i, k):
    j = 0  # variable initialized
    global num_calls
    num_calls += 1  # global variable incremented everytime quicksort is called
    if i >= k:
        return
    j = partition(user_ids, i, k)
    quicksort(user_ids, i, j)
    quicksort(user_ids, j + 1, k)
    return


# unit testing
if __name__ == "__main__":
    user_ids = []  # creates empty list
    user_id = input()  # takes user input
    while user_id != "-1":
        user_ids.append(user_id)  # user input is appended to user_ids list while the user input isn't "-1"
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
