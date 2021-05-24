from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to My Silent Auction App!\n")

# list of dictionaries for the bidder and bid and flag to stop bids
bids_dictionary = {}
more_bids = True

while more_bids == True:

  # prompt the user for their name and bid
  bidder = input("What is the bidder's name? ")
  bid = int(input (f"How much would {bidder} like to bid? $"))

  bids_dictionary[bidder] = bid

  more_bidders = input("Are there any other bidders? ")

  if more_bidders == "yes":
    clear()
  elif more_bidders == "no":
    more_bids = False
  else: 
    print("TRY AGAIN")

max_bid = 0
winner = ""

for bidder in bids_dictionary:
  if bids_dictionary[bidder] > max_bid:
    max_bid = bids_dictionary[bidder]
    winner = bidder

print(f"{winner} is the winner with a bid of ${max_bid}.")


