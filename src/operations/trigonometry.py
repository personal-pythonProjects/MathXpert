import math

class Trigonometry:
    def sine(self, num):
        return math.sin(math.radians(num))

    def cosine(self, num):
        return math.cos(math.radians(num))

    def tangent(self, num):
        try:
            return math.tan(math.radians(num))
        except ValueError:
            return "Error: Tangent undefined for this value"

    def sine_hyperbolic(self, num):
        return math.sinh(num)

    def cosine_hyperbolic(self, num):
        return math.cosh(num)

    def tangent_hyperbolic(self, num):
        return math.tanh(num)
