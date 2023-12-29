# importing useful libraries and modules
from Coffee_Data import MENU, resources

# inputing the customer's choice (Espresso, Latte, Cappucino)

# empty wallet
final_wallet = 0

# inputting the customer's money (Quarters, Dimes, Nickles, Pennies)
def money_collector():
    quarters_num = int(input("How many quartes do you have"))* 0.25 # quarter * 0.25 = quarter in dollar
    dimes_num = int(input("How many dimes do you have")) * 0.10
    nickles_num = int(input("How many nickels do you have")) * 0.05
    pennies_num = int(input("How many pennies do you have")) * 0.001
    customer_wallet = quarters_num + dimes_num + nickles_num + pennies_num
    return customer_wallet

final_wallet = money_collector()
print(f"Your total of coins in $ is {final_wallet}$")

# the order choosen by the client price
order_price = 0
def order_detail():
    customer_choice = input("Please Enter your wanted coffe:\nE for Esspresso \nL for Latte \n C for Cappuccino").lower
    if customer_choice == "e":
        order_price  = MENU["espresso"]["cost"]
        return order_price
    elif customer_choice == "l":
        order_price  = MENU["latte"]["cost"]
        return order_price
    elif customer_choice == "c":
        order_price  = MENU["cappuccino"]["cost"]
        return order_price
    else:
        print("please enter a valid coffee type")
final_price = order_detail()

    # elif customer_choice == "l"

    # else:


# # checking if the money is enough 
# if final_wallet > order_price
# # delivering th chosen type of coffee


