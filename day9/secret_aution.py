from art import logo

print(logo)

bid_over = False
bidders = {}


def highest_bidder(bid_dict):
    highest = 0
    winner = ''

    for top_bid in bid_dict:
        high_bid = bid_dict[top_bid]

        if high_bid > highest:
            highest = high_bid
            winner = top_bid

    return highest, winner


while not bid_over:
    user = input("What is your name? \n")
    user_bid = int(input("What is your bid: $"))
    another_user = input("Are there other bidders? 'Yes' or 'No'? ").strip().lower()
    bidders[user] = user_bid

    if another_user == 'no':
        bid_over = True
    elif another_user == 'yes':
        bid_over = False
    else:
        print("Invalid response. Bidding Over")
        bid_over = True

winner_bid, winner = highest_bidder(bidders)
print(f"The highest bidder is {winner} with a bid of ${winner_bid}")