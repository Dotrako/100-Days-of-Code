# Calculator Program
# n1 = float(input("Enter the first number"))
# n2 = float(input("Enter the second number"))

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

calculator = {"+": addition, 
              "-": substract, 
              "*": multiply,
              "/": division}

# for key in calculator:
#     print(key)

# for value in calculator.values():
#     print(value)