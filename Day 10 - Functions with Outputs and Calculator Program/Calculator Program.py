# Calculator Program

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

operations = {"+": addition, 
              "-": substract, 
              "*": multiply,
              "/": division,
}

num1 = float(input("Enter the first number"))

for symbol in operations:
    print(symbol)
operation_symbol = input("Please pick an opperation symbol (+, -, * or /)")
num2 = float(input("Enter the second number"))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
    
# for value in calculator.values():
#     print(value)
