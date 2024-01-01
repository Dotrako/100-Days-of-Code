#import modules and libraries
from Coffee_Data import MENU, resources


def is_ressource_sufficient(order_ingrdients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    is_enough = True
    for item in order_ingrdients:
        if order_ingrdients[item] >= resources[item]:
            print(f"Sorry there is not enough water.")
            is_enough = False
    return is_enough

def money_collector():
    """Collects money input from the customer and returns the total amount."""
    quarters_num = int(input("How many quartes do you have"))* 0.25 # quarter * 0.25 = quarter in dollar
    dimes_num = int(input("How many dimes do you have")) * 0.10
    nickles_num = int(input("How many nickels do you have")) * 0.05
    pennies_num = int(input("How many pennies do you have")) * 0.01
    customer_wallet = quarters_num + dimes_num + nickles_num + pennies_num
    return customer_wallet

def money_checker():
    """Checks if the customer has sufficient funds and calculates the change."""
    cost = MENU[choice]["cost"]
    
    if payment >= cost:
        change = payment - cost
        print(f"Your total money is {payment} $, here is your coffee and your change {round(payment - cost, 2)} $")
        return change
    else:
        print(f"You dont have enough money please insert mor coins, money refunded")
        return payment

# ask user about their order 
machine_is_on = True

profit = 0 

while machine_is_on:
    choice = input("What would you like? (espresso/latte/cappucino)").lower()
    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        print(f"{resources["water"]}")
        print(f"{resources["milk"]}")
        print(f"{resources["coffee"]}")
        print(f"money: $ {profit}")
        machine_is_on = False
    else:
        drink = MENU[choice]
        if is_ressource_sufficient(drink["ingredients"]):
            payment = money_collector()
            money = money_checker()
            machine_is_on = False