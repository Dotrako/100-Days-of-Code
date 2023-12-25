import random as rd
from Art import logo
print(logo)
# Allow the player to submit a guess for a number between 1 and 100.

guess = int(input("Please Enter a number between 1 and 100!"))
numbers_list = list()

def game_setup(game):
    for number in range(1,101):
        numbers_list.append(number)
    print(numbers_list)
game_setup(game = guess)

npc_number = rd.choice(numbers_list)
print(npc_number)

setup=[1,2,3]
difficulty = int(input("Please put your difficulty lvl 1 for easy 2 for medium and 3 for hard"))
number_of_guess = 0

def difficulty_setup(difficulty):
    global number_of_guess
    if difficulty == 1:
        print("you have chosen the easy difficulty you have 10 attempts")
        number_of_guess = 10
    elif difficulty == 2:
        print("you have chosen the medium difficulty you have 5 attempts")
        number_of_guess = 5
    elif difficulty == 3:
        print("you have chosen the hard difficulty you have only 3 attempts")
        number_of_guess = 3
difficulty_setup(difficulty)

def finish():
    pass
finish()
def guess_rules():
    global difficulty
    global npc_number
    zbi = False
    while not zbi: 
        for attempts in range(number_of_guess):
            guess = int(input("Please Enter a number between 1 and 100!"))
            if guess == npc_number:
                print(f"Congrats {npc_number} is the right number")
                finish()     
guess_rules()