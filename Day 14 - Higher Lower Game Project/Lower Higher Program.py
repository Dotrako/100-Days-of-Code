# Importing necessary libraries and modules
import random
import os
from Art import logo, vs
from game_data import data

# Function to get data from a random account
def get_random_account():
    """Get data from random account"""
    return random.choice(data)

# Function to format account data into a printable format
def format_data(account):
    """Format account into printable format: name, description, and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# Function to check if the user's guess is correct
def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Function to clear the console output
def clear():
    """Clears the console output based on the operating system."""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Linux and macOS
    else:
        _ = os.system('clear')

# Main game function
def game():
    # Display the game logo
    print(logo)
    score = 0
    game_should_continue = True
    
    # Get initial random accounts
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        # Update accounts for comparison
        account_a = account_b
        account_b = get_random_account()

        # Ensure different accounts are chosen for comparison
        while account_a == account_b:
            account_b = get_random_account()

        # Display account details for comparison
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        
        # Get user's guess and compare follower counts
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Clear the console and display game status
        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

# Start the game
game()
