import math

class ExponentialLogarithmic:
    def power(self, num1, num2):
        return num1 ** num2

    def exponential(self, num):
        return math.exp(num)

    def natural_log(self, num):
        if num > 0:
            return math.log(num)
        else:
            return "Error: Logarithm undefined for non-positive values"

    def log_base_10(self, num):
        if num > 0:
            return math.log10(num)
        else:
            return "Error: Logarithm undefined for non-positive values"
