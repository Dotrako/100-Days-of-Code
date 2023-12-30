# Importing necessary modules and data from external Coffee_Data module
from Coffee_Data import MENU, resources

# Get customer's choice for the coffee type wanted 
customer_choice = input("Please Enter your wanted coffe:\nE for Esspresso \nL for Latte \nC for Cappuccino").lower()

# empty wallet of customer
final_wallet = 0

# Function to collect money from the customer
def money_collector():
    """Collects money input from the customer and returns the total amount."""
    quarters_num = int(input("How many quartes do you have"))* 0.25 # quarter * 0.25 = quarter in dollar
    dimes_num = int(input("How many dimes do you have")) * 0.10
    nickles_num = int(input("How many nickels do you have")) * 0.05
    pennies_num = int(input("How many pennies do you have")) * 0.001
    customer_wallet = quarters_num + dimes_num + nickles_num + pennies_num
    return customer_wallet
final_wallet = money_collector()
print(f"Your total of coins in $ is {round(final_wallet,2)}$")

# Initialize variables for order details
order_price = 0
coffe = ""

# Function to determine the order price based on the customer's choice
def order_detail(order, order_choice):
    """Determines the order details and returns the price."""
    if customer_choice == "e":
        order_choice = "espresso"
        order  = MENU["espresso"]["cost"]
        return order
    elif customer_choice == "l":
        order_choice = "latte"
        order  = MENU["latte"]["cost"]
        return order
    elif customer_choice == "c":
        order_choice = "cappuccino"
        order  = MENU["cappuccino"]["cost"]
        return order
    else:
        print("please enter a valid coffee type")
final_price = order_detail(order = order_price, order_choice = coffe)

# the total of the change 
result = final_wallet - final_price

# Calculate the change and inform the customer
def money_checker(coffe_type):
    """Checks if the customer has sufficient funds and calculates the change."""
    global final_wallet
    global final_price
    print(coffe)
    if final_wallet > final_price:
        print(f"Here is your coffe {coffe} and your change {round(final_wallet - final_price,2)}")
        return result
    else:
        print(f"You dont have enough money please insert mor coins, you need {round(final_price - final_wallet, 2)}$ ")
        return final_wallet
money_checker(coffe)