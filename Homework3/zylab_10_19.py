# Luis Onate
# 1596900

# class representing information about item purchased
class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # calculates price and prints it
    def print_item_cost(self):
        print(self.item_name + " " + str(self.item_quantity) + " @ $" +
              str(self.item_price) + " = $" + str(self.item_quantity * self.item_price))

    # method that prints description of items purchased
    def print_item_description(self):
        print(self.item_name + ": " + self.item_description)


# class representing information about shopping cart
class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    # method that adds items to shopping cart
    def add_item(self):
        print("ADD ITEM TO CART")
        name = str(input("Enter the item name:"))
        print()
        description = str(input("Enter the item description:"))
        print()
        price = int(input("Enter the item price:"))
        print()
        quantity = int(input("Enter the item quantity:"))
        print()
        self.cart_items.append(ItemToPurchase(name, price, quantity, description))

    # method that removes items from shopping cart
    def remove_item(self):
        found = False
        print("REMOVE ITEM FROM CART")
        remove = str(input("Enter name of item to remove:\n"))
        i = 0
        for obj in self.cart_items:
            if obj.item_name == remove:
                del self.cart_items[i]
                found = True
                break
            else:
                found = False
                i += 1
        if not found:
            print("Item not found in cart. Nothing removed.")

    # method that modifies the quantity of an item in the shopping cart
    def modify_item(self):
        found = True
        print("CHANGE ITEM QUANTITY")
        change = str(input("Enter the item name:\n"))
        quantity = int(input("Enter the new quantity:\n"))
        for obj in self.cart_items:
            if obj.item_name == change:
                obj.item_quantity = quantity
                found = True
            else:
                found = False
        if not found:
            print("Item not found in cart. Nothing modified.")

    # method that retrieves amount of items in shopping cart
    def get_num_items_in_cart(self):
        object_amount = 0
        for i in self.cart_items:
            object_amount += i.item_quantity
        return object_amount

    # method that calculates total amount for items in the shopping cart
    def get_cost_of_cart(self):
        total_amount = 0
        for i in self.cart_items:
            total_amount = total_amount + (i.item_price * i.item_quantity)
        return total_amount

    # method that prints the total amount in cart
    def print_total(self):
        total_amount = self.get_cost_of_cart()
        if total_amount == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            self.output_cart()

    # method that prints shopping cart item descriptions
    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("\nItem Descriptions")
            for obj in self.cart_items:
                obj.print_item_description()

    # method that displays shopping cart items
    def output_cart(self):
        print("OUTPUT SHOPPING CART")
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Number of Items:", self.get_num_items_in_cart())
        print()
        total_amount = 0
        for obj in self.cart_items:
            print("{} {} @ ${} = ${}".format(obj.item_name, obj.item_quantity,
                                             obj.item_price, (obj.item_quantity * obj.item_price)))
            total_amount += (obj.item_quantity * obj.item_price)
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        print()
        print("Total: ${}".format(total_amount))


# unit test
if __name__ == "__main__":
    def print_menu(cart):  # prints the menu with options for users
        menu = ("\nMENU\n"
                "a - Add item to cart\n"
                "r - Remove item from cart\n"
                "c - Change item quantity\n"
                "i - Output items' descriptions\n"
                "o - Output shopping cart\n"
                "q - Quit\n")
        option = ''
        while option != 'q':  # exits loop with input of q
            print(menu)
            option = input("Choose an option:")
            print()
            while (option != 'a' and option != 'o' and option != 'i' and option != 'r'
                   and option != 'c' and option != 'q'):
                option = input("Choose an option:")
                print()
            if option == 'a':  # adds item to cart with input of a
                cart.add_item()
            if option == 'o':  # displays shopping cart with input of o
                cart.output_cart()
            if option == 'i':  # prints item descriptions with input of i
                cart.print_descriptions()
            if option == 'r':  # removes items from shopping cart with input of r
                cart.remove_item()
            if option == 'c':  # modifies amount for items in shopping cart with input of c
                cart.modify_item()


    customer_name = str(input("Enter customer's name:\n"))  # request user's name
    current_date = str(input("Enter today's date:\n\n"))  # requests current data from user
    print("Customer name:", customer_name, end='\n')  # prints users name
    print("Today's date:", current_date, end='\n')  # prints the current date
    cart_1 = ShoppingCart(customer_name, current_date)  # calls the ShoppingCart class with user inputs as parameters
    print_menu(cart_1)  # prints the menu for user inputs
