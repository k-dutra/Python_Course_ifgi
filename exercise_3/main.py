#script created to test the modules
#OBS: it was used before the package easy_shopping was created

import calculator

calc = calculator.Calculator()

print(calc.addition(7,5))
print(calc.subtraction(34,21))
print(calc.multiplication(54,2))
print(calc.division(144,2))
print(calc.division(45,0))


import shopping

item1 = shopping.Shopping_cart("Apfelshorle", 2, 1.5)
item2 = shopping.Shopping_cart("Milch", 3, 1.15)
item3 = shopping.Shopping_cart("Olivenöl", 1, 9.2)

#display the items and quantity and calculate the total of items
for item in shopping.Shopping_cart.all_cartinfo:
    print(item.item, item.qt)

#calculate the quantity of items in the cart
shopping.Shopping_cart.total_qtitems()

#remove itens, display the updated list and calculate the total of items
shopping.Shopping_cart.all_cartinfo.remove(item1)
shopping.Shopping_cart.total_qtitems()

#extra: calculate the total value in euros in the cart
shopping.Shopping_cart.total_price()