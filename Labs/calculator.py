import math_utils

def main():
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /, **, %): ")

        operations = {
            '+': math_utils.add,
            '-': math_utils.subtract,
            '*': math_utils.multiply,
            '/': math_utils.divide,
            '**': math_utils.power,
            '%': math_utils.mod,
        }

        if operator in operations:
            result = operations[operator](x, y)
            print("Result:", result)
        else:
            print("Invalid operator")

    except ValueError:
        print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    main()
