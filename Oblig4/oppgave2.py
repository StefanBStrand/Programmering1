# Lets play blackjack!

# Components to make:
#  Blackjack class (holding info about game rules?)
# How to shuffle/pick cards? --> randomization method, rand-range?
#  List to hold all the prompts/questions?
#  One list for dealer hand and one list for player hand.


class Player:
    def __init__(self, chips, bet, player_score):
        self.chips = chips
        self.bet = bet
        self.score = player_score


class Dealer:
    def __init__(self, dealer_score, action):
        self.dealer_score = dealer_score
        self.action = action


# The following code is for creating the deck of cards needed to play the game:

class Card:  # creating a Card class to represent the special attributes of a deck of cards.
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.rank} of {self.suit}"  # If trying to print out deck without the repr method, it will
    #  print out a not so human friendly printout.


ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]  # List of card ranks
suits = ["Hearts", "Clubs", "Spades", "Diamonds"]  # List of card suits.

deck = []  # empty list to store my deck, once created with the help of a for-loop.

for card_suit in suits:
    for card_rank in ranks:
        if card_rank == "Ace":
            card_value = 11  # Ace needs to be handled within the function, in case it should be valued as 1 instead.
        elif card_rank in ["Jack", "Queen", "King"]:
            card_value = 10
        else:
            card_value = int(card_rank)

        card = Card(card_rank, card_suit, card_value)
        deck.append(card)

for card in deck:
    print(card)  # Printing out the deck to see if this is correct. Looping it makes it easier to read.

# End of code creating a deck of cards.


prompts = []
player_hand = []
dealer_hand = []

hit_or_stand = {
    1: "hit",
    2: "stand"
}

playing = True


def play_blackjack():
    while playing:
        Dealer.dealer_score = 0
        Player.player_score = 0
        Player.chips = 3000
