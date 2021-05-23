from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to My Silent Auction App!\n")

# list of dictionaries for the bidder and bid and flag to stop bids
list_of_bids = []
more_bids = True

def add_new_bid(bidder, bid):
  list_of_bids.append(
    {
      "bidder_name": bidder,
      "bid_amount": bid
    }
  )


while more_bids == True:

  # prompt the user for their name and bid
  bidder = input("What is the bidder's name? ")
  bid = int(input (f"How much would {bidder} like to bid? $"))

  add_new_bid(bidder, bid)

  more_bidders = input("Are there any other bidders? ")

  if more_bidders == "yes":
    clear()
  elif more_bidders == "no":
    more_bids = False
  else: 
    print("TRY AGAIN")

max_bid = 0

total_bids = [a_dict["bid_amount"] for a_dict in list_of_bids]

print(max(total_bids))
