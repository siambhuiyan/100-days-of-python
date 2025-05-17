bids = {}

continue_bidding = True


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid =0
    
    max(bidding_dictionary, key=bidding_dictionary.get)

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while continue_bidding:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        continue_bidding = True
        print("\n" * 100)
        
    


