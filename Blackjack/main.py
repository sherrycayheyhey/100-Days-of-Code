from art import logo
import random

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


# draw a card from the "cards" list
def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def sum_cards(hand):
    # check for a blackjack, return 0 if it is
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    # if the hand would go over 21, change the ace from 11 to 1
    if 11 in hand and sum_cards(hand) > 21:
        hand[hand.index(11)] = 1
    return sum(hand)


def play_game():
    print(logo)

    stand = False

    # deal the player two cards and display them on the screen
    # create empty hands for the player and dealer
    player_cards = []
    dealer_cards = []

    # deal 2 cards each
    for _ in range(2):
        player_cards.append(draw_card())
        dealer_cards.append(draw_card())
        # append has to be used when adding a single item to a list, not +=

    # calculate the player's total so far and show the cards
    player_total = sum_cards(player_cards)
    print(f"Your cards: {player_cards}, current score: {player_total}")

    # show the dealer's first card
    print(f"Dealer's first card: {dealer_cards[0]}\n")

    while player_total < 21 and not stand:
        # ask player to hit or stand
        action = input("'hit' for another card or 'stand' to end your turn: ")

        if action == "hit":
            player_cards.append(draw_card())
            player_total = sum(player_cards)
            if 11 in player_cards and player_total > 21:
                player_cards[player_cards.index(11)] = 1
                player_total = sum(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_total}\n")
        elif action == "stand":
            print("")
            stand = True
        else:
            print("that wasn't an option")

    print(f"Your final hand: {player_cards}, final score: {player_total}")

    dealer_total = sum_cards(dealer_cards)

    # player has ended turn, dealer draws cards if total is less than 16
    while dealer_total < 17 and player_total <= 21:
        dealer_cards.append(draw_card())
        dealer_total = sum(dealer_cards)

    # display computer's cards and total
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_total}\n")

    # compare totals for game result
    if player_total > 21:
        if dealer_total <= 21:
            print("player busts, the house wins")
        else:
            print("you both bust, hah")
    elif dealer_total > 21 >= player_total:
        print("the house busts, player wins")
    elif dealer_total < player_total <= 21:
        print("player wins")
    elif player_total < dealer_total <= 21:
        print("the house wins")
    else:
        print("it was a tie, yall")
    print("")


# ask the user if they want to play
while input("Do you want to play blackjack? Type 'y' or 'n': ") == "y":
    play_game()

exit()
