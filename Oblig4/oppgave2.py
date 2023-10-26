# Lets play blackjack!

# Components to make:
#  Blackjack class (holding info about game rules?)
# How to shuffle/pick cards? --> randomization method, rand-range?
#  List to hold all the prompts/questions?
#  One list for dealer hand and one list for player hand.

import random


STARTING_CHIPS = 3000


class Player:
    def __init__(self):
        self.chips = STARTING_CHIPS
        self.bet = 0
        self.player_score = 0
        self.player_hand = []


player1 = Player()  # Creating an object(instance of the class Player)


class Dealer:
    def __init__(self):
        self.dealer_score = 0
        self.dealer_hand = []


dealer = Dealer()  # creating an object(instance of the class Dealer)


# ***** The following code is for creating the deck of cards needed to play the game: *****

class Card:  # creating a Card class to represent the special attributes of a card (in a deck of cards).
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.rank} of {self.suit}"  # If trying to print out deck without the repr method, it will
    #  print out a not so human friendly printout.

    def __str(self):
        return self.__str()


# code to create 6 decks to use in game: wrapping the deck-creating for-loop in for loop of its own,
# iterating 6 times and adding to master_deck.

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]  # List of card ranks
suits = ["Hearts", "Clubs", "Spades", "Diamonds"]  # List of card suits.


master_deck = []

for i in range(6):
    for card_suit in suits:
        for card_rank in ranks:
            if card_rank == "Ace":
                card_value = 11
                # Ace needs to be handled within the function, in case it should be valued as 1 instead.
            elif card_rank in ["Jack", "Queen", "King"]:
                card_value = 10
            else:
                card_value = int(card_rank)

            card = Card(card_rank, card_suit, card_value)  # making an instance of the Card class.
            master_deck.append(card)

# for card in master_deck:
    # print(card.value)  # Printing out the deck to see if this is correct. Looping it makes it easier to read.

# ***** End of code creating a deck of cards. *****

# ***** Creating blackjack variable *****

face_cards = [card for card in master_deck if card.rank in ["Jack", "Queen", "King"]]
aces = [card for card in master_deck if card.rank == "Ace"]



# Components for blackjack:

# player_hand = [] Swapped for attribute in Player class
# dealer_hand = [] Swapped for attribute in Dealer class

hit_or_stand = {
    1: "hit",
    2: "stand"
}

playing = True


def play_blackjack():
    while playing:
        dealer.dealer_score = 0
        player1.player_score = 0
        try:
            # player1.chips = 3000. Replaced with STARTING_CHIPS
            new_deal = int(input(f"Place your bet! You currently have {player1.chips} chips. How much ya bettin'?:"))
        except ValueError:
            print("Invalid betting! Please enter a valid bet number.")
            continue  # jumps to next iteration of loop, prompting user for new input.

        if new_deal > player1.chips:
            print("You cannot bet more chips than you have in total")
        elif new_deal <= 0:
            print("Please place a bet greater than 0")
        else:
            player1.bet = int(new_deal)
            player1.chips -= player1.bet
            print(f"You bet {new_deal} chips. You now have {player1.chips} chips remaining")
            random.shuffle(master_deck)
            player1.player_hand.append(master_deck.pop())
            player1.player_hand.append(master_deck.pop())


            # I NEED TO ADD THE VALUES OF THE GIVEN CARDS TOGETHER _ FIXED

            for card in player1.player_hand:
                player1.player_score += card.value

            # NOW I NEED TO MAKE THE BLACKJACK CHECK WORK - FIX THIS FRIDAY! COde GOES HERE

            dealer.dealer_hand.append(master_deck.pop())
            dealer.dealer_hand.append(master_deck.pop())

            if player1.player_hand == aces and face_cards:
                player1.bet += player1.bet * 3
                player1.chips += player1.bet
                print(f"{player1.player_hand} Blackjack! You win 2x your bet!")
                continue
            else:
                print(f"Cards have been dealt. You have {player1.player_hand} with a value of {player1.player_score}")


#play_blackjack()

