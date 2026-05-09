# Class to perform addition, subtraction, multiplication and division calculus.
#When the division has a denominator equals to zero it retuns an error message.

class Calculator:

    def addition(self, x, y):
        return x+y
    
    def subtraction(self, x, y):
        return x-y
    
    def multiplication(self, x, y):
        return x*y
    
    def division(self, x, y):
        try:
            return x/y
        except ZeroDivisionError:
            return "Error: division by 0 is undefined."
        