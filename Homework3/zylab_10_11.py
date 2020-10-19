# Luis Onate
# 1596900

# class representing information about a food item
class FoodItem:
    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    # definition for printing information about food item
    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


# unit testing
if __name__ == '__main__':
    food1 = FoodItem()  # first call of class FoodItem with empty parameters
    # second call of class FoodItem with user input parameters
    food2 = FoodItem(input(), float(input()), float(input()), float(input()))
    serving = float(input())  # user input parameter for num_servings in calorie formula
    food1.print_info()  # print information for first calling of class FoodItem with empty parameters
    print('Number of calories for {:.2f} serving(s): {:.2f}\n'
          .format(serving, food1.get_calories(serving)))  # print calorie information for first calling of class
    food2.print_info()  # print information for second calling of class FoodItem with user input parameters
    print('Number of calories for {:.2f} serving(s): {:.2f}'
          .format(serving, food2.get_calories(serving)))  # print calorie information for second calling of class
