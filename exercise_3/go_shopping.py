#script to import easy_shopping and test it

import easy_shopping

#instantiate calculator
calc = easy_shopping.calculator.Calculator()

#test calculator class
easy_shopping.calc.addition(7,5)
easy_shopping.calc.multiplication(54,2)
easy_shopping.calc.division(45,0)

#test shopping class
item1 = easy_shopping.shopping.Shopping_cart("Apfelshorle", 2, 1.5)
item2 = easy_shopping.shopping.Shopping_cart("Milch", 3, 1.15)

#print the items and the total of items
for item in easy_shopping.shopping.Shopping_cart.all_cartinfo:
    print(item.item, item.qt)

#calculate the quantity of items in the cart
easy_shopping.shopping.Shopping_cart.total_qtitems()