#using a class to program a calculator

class Calculator():
    """Calculator that executes the basic arithmetic operations"""
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def add(self):
        return self.x + self.y

    def substract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y

