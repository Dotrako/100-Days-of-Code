import os

bid_holder = dict()
bidding_finished = False

def find_highest_bid(bidding_record):
    highest_bid = 0 
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of £{highest_bid}")

while not bidding_finished:
    name = input("Please enter your name")
    price = int(input("Please place your bid"))
    should_continue = input("Are They any other bidders? Yes or No").lower()
    bid_holder = {"Name": name, "Bid": price}

    # Check if the user entered "Yes" (case-insensitive)
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        # Clear the output based on the operating system (linux/Macos or Windows)
        os.system("clear" if os.name == "posix" else "cls")
    
        # Additional code or message after clearing the output can be added here
        print("Output cleared!")
print(bid_holder)