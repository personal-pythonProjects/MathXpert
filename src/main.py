import art
from src.handlers.operation_handler import OperationHandler

def available_operations(calculator):
    print("\nBasic Arithmetic:")
    print("-" * 30)
    for operator in calculator.basic_operations.keys():
        print(operator, end=', ')

    print("\n\nExponential and Logarithmic:")
    print("-" * 30)
    for operator in calculator.exponential_operations.keys():
        print(operator, end=', ')

    print("\n\nPower and Root:")
    print("-" * 30)
    for operator in calculator.power_root_operations.keys():
        print(operator, end=', ')

    print("\n\nTrigonometric Functions:")
    print("-" * 30)
    for operator in calculator.trigonometric_operations.keys():
        print(operator, end=', ')

    print("\n\nFactorial:")
    print("-" * 30)
    for operator in calculator.factorial_operations.keys():
        print(operator, end=', ')

    print("\n\nRandom:")
    for operator in calculator.random_operations.keys():
        print(operator, end=', ')

if __name__ == "__main__":

    def perform_calculation():
        try:
            print(art.logo)
            calculator = OperationHandler()
            continue_calculating = True
            decimal_places = int(input("Enter the number of decimal places for results: "))

            while continue_calculating:
                print("Available operations:")
                available_operations(calculator)

                selected_operation = input("\n\nChoose an operations: ")
                calculation_function = calculator.operations_map.get(selected_operation)

                if calculation_function:
                    if selected_operation in calculator.random_operations.keys():
                        start = float(input("Enter the start range: "))
                        end = float(input("Enter the end range: "))
                        result = calculation_function(start, end)
                    elif (selected_operation in calculator.exponential_operations.keys()
                            or selected_operation in calculator.power_root_operations.keys()
                            or selected_operation in calculator.trigonometric_operations.keys()
                            or selected_operation in calculator.factorial_operations.keys()):
                        num = float(input("Enter the number: "))
                        result = calculation_function(num)
                    elif selected_operation in calculator.basic_operations.keys():
                        num1 = float(input("Enter the first number: "))
                        while True:
                            num2 = float(input("Enter the next number: "))
                            result = calculation_function(num1, num2)
                            if isinstance(result, (int, float)):
                                result = round(result, decimal_places)
                            print(f"\n{num1} {selected_operation} {num2} = {result}")
                            num1 = result
                            next_choice = input("Type 'y' to continue with this operation, or 'n' to exit this operations: ")
                            if next_choice.lower() != 'y':
                                break
                    else:
                        num1 = float(input("Enter the first number: "))
                        num2 = float(input("Enter the second number: "))
                        result = calculation_function(num1, num2)

                    if isinstance(result, (int, float)):
                        result = round(result, decimal_places)
                    print(f"\n{num1 if 'num1' in locals() else ''} {selected_operation} {num2 if 'num2' in locals() else ''} = {result}")

                    user_choice = input(f"Type 'y' to continue calculating, or 'n' to exit: ")

                    if user_choice.lower() == 'y':
                        current_result = result
                    else:
                        continue_calculating = False
                        print("\n" * 20)
                        perform_calculation()
                else:
                    print("Invalid operation selected. Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")

    perform_calculation()