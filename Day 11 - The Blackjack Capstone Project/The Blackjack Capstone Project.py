import random 
from Art import logo
print(logo)

n1 = 0 
n2 = 0
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def addition(num1, num2):
    return num1 + num2

choice1 = (input("Do you want to play a game of Blackjack? Type 'y' or 'n':"))

user_deck = list()
computer_card = list()

if choice1 == "y":
    user_deck.append(random.choice(deck))
    user_deck.append(random.choice(deck))
    computer_card.append(random.choice(deck))
    print(f"Your cards: {user_deck}, current score is {addition(user_deck[0], user_deck[1])}")
    print(f"The Computer first card is {computer_card}")
    choice2 = input("Please Enter your decision 'h' for Hit and 's' for Stand").lower()
    if choice2 == "h":
        user_deck.append(random.choice(deck))
        


    
else:
    print("Thank you for visiting our game, see you next")


