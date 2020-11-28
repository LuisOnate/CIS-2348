# Luis Onate
# 1596900

# function that computes the fat burning heart rate
def fat_burning_heart_rate(age):
    fat_rate = .70 * (220 - age)  # the calculation is assigned to the variable fat_rate
    return fat_rate


# function that gets age from the user
def get_age():
    age = int(input())  # user inputted age is assigned to the variable age
    if (age <= 18) or (age >= 75):  # if the age is less than 18 or over 75---
        raise ValueError('Invalid age.')  # ---the value error is raised
    return age  # age is returned so that it may be used outside function


# unit testing
if __name__ == "__main__":
    try:
        # the function for getting the age is called
        get_age = get_age()
        # the function for calculating the fat burning heart rate is called with the return of get_age as the parameter
        rate = fat_burning_heart_rate(get_age)
        print('Fat burning heart rate for a', get_age, 'year-old:', rate, 'bpm')

    # the exception value error that tells the user when an age input is invalid for fat burning heart rate calculation
    except ValueError as excpt:
        print(excpt)
        print('Could not calculate heart rate info.\n')
