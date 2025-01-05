import math

class PowerRoot:
    def square(self, num):
        return num ** 2

    def cube(self, num):
        return num ** 3

    def square_root(self, num):
        if num >= 0:
            return math.sqrt(num)
        else:
            return "Error: Square root undefined for negative values"

    def cube_root(self, num):
        return math.cbrt(num)