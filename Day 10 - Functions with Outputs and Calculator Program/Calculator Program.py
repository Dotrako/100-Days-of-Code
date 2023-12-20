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
num2 = float(input("Enter the second number"))

operation_symbol = input("Please pick an opperation symbol (+, -, * or /)")

if operation_symbol == "+":
        result = addition(num1,num2)
elif operation_symbol == "-":
        result = substract(num1, num2)
elif operation_symbol == "*":
        result = multiply(num1, num2)
elif operation_symbol == "/":
        result = division(num1, num2)
else:
    print("Please choose a right operator!")

print(f"{num1} {operation_symbol} {num2} = {result}")
    
# for value in calculator.values():
#     print(value)