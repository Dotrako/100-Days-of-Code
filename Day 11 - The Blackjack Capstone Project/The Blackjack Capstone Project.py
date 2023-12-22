import random
from Art import logo

print(logo)

def calculate_total(cards):
    """Calculate the total value of a list of cards."""
    total = sum(cards)
    return total

def draw_card(deck):
    """Draw a card from the deck."""
    return random.choice(deck)

while True:
    user_hand = []
    pc_hand = []
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # User's initial draw
    user_hand.append(draw_card(deck))
    user_hand.append(draw_card(deck))
    print(f"Your initial hand: {user_hand}")
    user_total = calculate_total(user_hand)
    print(f"Your total: {user_total}")

    # Dealer's initial draw
    pc_hand.append(draw_card(deck))
    print(f"Dealer's first card: {pc_hand[0]}")

    # User's turn
    while True:
        action = input("Type 'H' to hit or 'S' to stand: ").lower()
        if action == "h":
            user_hand.append(draw_card(deck))
            print(f"Your hand: {user_hand}")
            user_total = calculate_total(user_hand)
            print(f"Your total: {user_total}")
            if user_total > 21:
                print("Bust! You lose.")
                break
        elif action == "s":
            break
        else:
            print("Invalid input. Try again.")

    # Dealer's turn
    pc_total = calculate_total(pc_hand)
    while pc_total < 17:
        pc_hand.append(draw_card(deck))
        pc_total = calculate_total(pc_hand)

    print(f"Dealer's hand: {pc_hand}")
    print(f"Dealer's total: {pc_total}")

    # Determine the winner
    if user_total > 21:
        print("You lose.")
    elif pc_total > 21:
        print("You win!")
    elif user_total > pc_total:
        print("You win!")
    elif user_total < pc_total:
        print("You lose.")
    else:
        print("It's a tie.")

    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again != "y":
        break
