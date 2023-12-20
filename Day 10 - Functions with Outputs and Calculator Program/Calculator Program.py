# Calculator Program
from Art import logo
# Addition
def addition(n1, n2):
    return n1 + n2

# Substraction 
def substract(n1, n2):
    return n1 - n2

# Multiplication 
def multiply(n1, n2):
    return n1 * n2

# Division
def division(n1,n2):
    return n1 / n2

# var = input("Enter y to continue and n to finish").lower()

def calculator():
    print(logo)
    operations = {"+": addition, 
                "-": substract, 
                "*": multiply,
                "/": division,
    }

    num1 = float(input("Enter the first number"))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Please pick an opperation symbol (+, -, * or /)")
        num2 = float(input("Enter the second number"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to exit:") == "y":
            num1 = answer 
        else:
            should_continue = False
            calculator()  
calculator()

    # operation_symbol = input("Please pick an opperation symbol (+, -, * or /)")
    # num3 = float(input("Enter the next number"))
    # calculation_function = operations[operation_symbol]
    # # answer2 = calculation_function(calculation_function(num1, num2), num3)
    # answer2 = calculation_function(answer1, num3)

    # print(f"{answer1} {operation_symbol} {num3} = {answer2}")
    # var = input("Enter y to continue and n to finish").lower()

    # # for value in calculator.values():
    # #     print(value)
