import os
clear = lambda: os.system('cls')

from art import logo
print(logo)

bids = {}
bid_completed = False

def find_highest_bidder(bidding_record):
    max_price = 0
    for bidder in bidding_record:
        price = bidding_record[bidder]
        if price > max_price :
            max_price = price
            winner  = bidder
    print(f"The winner is {winner} with a bid of ${max_price}")

while not bid_completed:
    name = input("Enter the name of bidder: ")
    price = int(input("Enter your price: &"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'y' or 'n'.\n")

    if should_continue == 'n':
        bid_completed = True
        find_highest_bidder(bids)
    else:
        clear()
