#Class to be use as a shopping list. 
# Items can be added, displayed and the quantity of items can be counted.
#extra: I added an extra atribute to store the individual price, 
# and a method to calculate the total amount of the cart.

class Shopping_cart: 

    all_cartinfo = []   # class variable shared by all objects

    def __init__(self, item, qt, price):
        self.item = item
        self.qt = qt
        self.price = price

        Shopping_cart.all_cartinfo.append(self) #store all information of items in cart

    @classmethod
    def total_qtitems(cls):
         total = sum(item.qt for item in cls.all_cartinfo)
         print(f'{total} items in the cart')

    @classmethod
    def total_price(cls):
        sum_price = sum(item.price * item.qt for item in cls.all_cartinfo)
        print(f'{sum_price:.2f} euros is the monetary amount in cart')