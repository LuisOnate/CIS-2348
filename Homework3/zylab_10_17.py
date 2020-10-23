# Luis Onate
# 1596900

# class representing information about item purchased
class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # calculates price and prints it
    def print_item_cost(self):
        price = self.item_price * self.item_quantity
        print('{} {} @ ${} = $'.format(self.item_name, self.item_quantity, self.item_price), price, sep='')


# unit test
if __name__ == '__main__':
    item1 = ItemToPurchase()  # object one of ItemToPurchase class
    print('Item 1')
    print('Enter the item name:')
    item1.item_name = input()
    print('Enter the item price:')
    item1.item_price = int(input())
    print('Enter the item quantity:')
    item1.item_quantity = int(input())
    print()

    item2 = ItemToPurchase()  # object two of ItemToPurchase class
    print('Item 2')
    print('Enter the item name:')
    item2.item_name = input()
    print('Enter the item price:')
    item2.item_price = int(input())
    print('Enter the item quantity:')
    item2.item_quantity = int(input())
    print()

    print('TOTAL COST')
    item1.print_item_cost()  # call to print cost for object one
    item2.print_item_cost()  # call to print cost for object two

    # calculates the sum of both prices for the two items
    total = int((item1.item_quantity * item1.item_price) + (item2.item_quantity * item2.item_price))
    print('\nTotal: $', total, sep='')  # prints total cost of both items
