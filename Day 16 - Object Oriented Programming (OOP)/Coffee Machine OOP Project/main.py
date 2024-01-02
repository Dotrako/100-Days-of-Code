# Import necessary classes from modules
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initialize MoneyMachine, CoffeeMaker, and Menu objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Set the initial state of the coffee machine to 'on'
is_on = True

# Main loop to keep the coffee machine running
while is_on:
    # Get available menu items
    options = menu.get_items()
    
    # Prompt user for choice
    choice = input(f"What would you like? ({options}): ")
    
    # Check for special commands
    if choice == "off":
        is_on = False  # Turn off the coffee machine
    elif choice == "report":
        # Generate and display reports for coffee and money resources
        coffee_maker.report()
        money_machine.report()
    else:
        # Find the selected drink from the menu
        drink = menu.find_drink(choice)
        
        # Check if there are enough resources and process payment
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Make the selected coffee
            coffee_maker.make_coffee(drink)
