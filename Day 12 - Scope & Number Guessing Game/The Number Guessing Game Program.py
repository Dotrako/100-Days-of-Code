import random as rd
from Art import logo

# Display the game logo
print(logo)

# Function to set up the game with numbers from 1 to 100
def game_setup():
    numbers_list = list(range(1, 101))
    print(numbers_list)
    return numbers_list

# Player's initial guess
guess = int(input("Please Enter a number between 1 and 100: "))

# Set up the game with available numbers
numbers_list = game_setup()

# Randomly select a number for the NPC (Non-Player Character)
npc_number = rd.choice(numbers_list)
print(f"The NPC's number is: {npc_number}")

# Get user input for game difficulty
difficulty = int(input("Please select your difficulty level (1 for easy, 2 for medium, 3 for hard): "))

# Set up game difficulty based on user input
def difficulty_setup(difficulty):
    global number_of_guess
    if difficulty == 1:
        print("You have chosen easy difficulty. You have 10 attempts.")
        number_of_guess = 10
    elif difficulty == 2:
        print("You have chosen medium difficulty. You have 5 attempts.")
        number_of_guess = 5
    elif difficulty == 3:
        print("You have chosen hard difficulty. You have only 3 attempts.")
        number_of_guess = 3

# Call the function to set up the game difficulty
difficulty_setup(difficulty)

# Function to handle the end of the game
def finish():
    print("Game Over!")
    # Add any additional end-of-game logic here

# Function to handle game rules and player's guesses
def guess_rules():
    global npc_number
    global number_of_guess
    for attempts in range(number_of_guess):
        guess = int(input("Please Enter a number between 1 and 100: "))
        if guess == npc_number:
            print(f"Congratulations! {npc_number} is the correct number.")
            finish()
            break
        elif guess > npc_number:
            print("Incorrect guess. Try again. Youre too High")
        else:
            print("Incorrect guess. Try again. Youre too Low")
    else:
        print(f"Sorry, you've run out of attempts. The correct number was {npc_number}.")
        finish()

# Start the game
guess_rules()