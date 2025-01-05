from src.operations.basic_arithmetic import BasicArithmetic
from src.operations.exponential_logarithmic import ExponentialLogarithmic
from src.operations.factorial import Factorial
from src.operations.power_root import PowerRoot
from src.operations.random_operations import RandomOperations
from src.operations.trigonometry import Trigonometry


class OperationHandler(BasicArithmetic,
                       ExponentialLogarithmic,
                       PowerRoot,
                       Trigonometry,
                       Factorial,
                       RandomOperations):

    def __init__(self):
        super().__init__()

        self.basic_operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }

        self.exponential_operations = {
            "^": self.power,
            "e^x": self.exponential,
            "ln": self.natural_log,
            "log10": self.log_base_10
        }

        self.power_root_operations = {
            "square": self.square,
            "cube": self.cube,
            "sqrt": self.square_root,
            "cbrt": self.cube_root
        }

        self.trigonometric_operations = {
            "sin": self.sine,
            "cos": self.cosine,
            "tan": self.tangent,
            "sinh": self.sine_hyperbolic,
            "cosh": self.cosine_hyperbolic,
            "tanh": self.tangent_hyperbolic
        }

        self.factorial_operations = {
            "fact": self.factorial
        }

        self.random_operations = {
            "rand": self.random_number
        }

        self.operations_map = {
            **self.basic_operations,
            **self.exponential_operations,
            **self.power_root_operations,
            **self.trigonometric_operations,
            **self.factorial_operations,
            **self.random_operations
        }

