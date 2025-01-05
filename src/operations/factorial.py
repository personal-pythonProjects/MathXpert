import math

class Factorial:
    def factorial(self, num):
        if isinstance(num, float) and num.is_integer():
            num = int(num)
        if isinstance(num, int) and num >= 0:
            return math.factorial(num)
        else:
            return "Error: Factorial only defined for non-negative integers"