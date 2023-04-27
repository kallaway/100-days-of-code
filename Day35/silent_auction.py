from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

all_bids = {}
bidding_done = False

def highest_bidder(total_bidders):
    highest_bid = 0
    winner = ""
    for bidder in total_bidders:
        bid_amount = total_bidders[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_done:
    name = input("What is your name?:")
    # make sure to declare price as int
    bid = int(input("What is your bid?: $"))
    all_bids[name] = bid
    other_bidders = input("Are there more bidders? 'yes' or 'no'")
    if other_bidders == "no":
        bidding_done = True
        highest_bidder(all_bids)
    elif other_bidders == "yes":
        clear()
    
