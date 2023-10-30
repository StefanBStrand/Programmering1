# Lets play blackjack!

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
        return f"{self.rank} of {self.suit}"  # If trying to print out cards without the repr method it will
    # print a very non-human friendly way of reading the cards. repr method returns string representation
    # of the object. I need this in order for my dealt cards to be understandable.


# **** Code to create 6 decks to use in game: wrapping the deck-creating for-loop in for loop of its own,
# iterating 6 times and adding to master_deck. Total of 312 cards to play with (Standard casino practice).

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]  # List of card ranks
suits = ["Hearts", "Clubs", "Spades", "Diamonds"]  # List of card suits.

master_deck = []


def get_new_deck():
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
    return master_deck


master_deck = get_new_deck()  # made function in order to re-initialize deck for each round, but not working so far.


def give_hit_or_stand_prompt():
    hit_or_stand = input("Do you wish to hit or stand? \n 1 - Hit \n 2 - Stand \n What will it be?:")
    try:
        hit_or_stand_decision = int(hit_or_stand)  # have to make input into int, otherwise crashes (valueError)
        # put this in a try/except block to make sure program does not crash.

        if hit_or_stand_decision not in [1, 2]:
            print("Invalid choice. Choose 1 for Hit and 2 for stand")
            return give_hit_or_stand_prompt()
    except ValueError:
        print("Invalid choice. Choose 1 for Hit and 2 for stand")
        return give_hit_or_stand_prompt()

    return hit_or_stand_decision


def check_winner():
    if dealer.dealer_score > player1.player_score:
        print("Dealer wins!")
    elif dealer.dealer_score == player1.player_score:
        print("Split, dealer and player equal score. No one wins.")
        player1.chips += player1.bet
    else:
        print("You win")
        player1.bet += player1.bet * 2
        player1.chips += player1.bet


def play_blackjack():
    while True:  # while loop so player can decide on his own when to stop.
        print(len(master_deck))  # Deck depletes as round go on if funct. not restarted. Just a check.
        random.shuffle(master_deck)  # shuffling deck for each round.
        dealer.dealer_score = 0  # resetting dealer score to zero for each round.
        player1.player_score = 0  # resetting player score to zero for each round.
        player1.player_hand = []  # resetting player hand to empty list for each round.
        dealer.dealer_hand = []  # resetting dealer hand to zero for each round
        try:
            new_deal = int(input(f"Place your bet! You currently have {player1.chips} chips. How much ya bettin'?:"))
        except ValueError:
            print("Invalid betting! Please enter a valid bet number.")  # try/except to not crash program.
            continue  # jumps to next iteration of loop, prompting user for new input.

        if new_deal > player1.chips:
            print("You cannot bet more chips than you have in total")
        elif new_deal <= 0:
            print("Please place a bet greater than 0")
        else:
            player1.bet = int(new_deal)  # setting user bet(input) to int (default is string)
            player1.chips -= player1.bet  # deducting bet amount from total amount of chips
            print(f"You bet {new_deal} chips. You now have {player1.chips} chips remaining")

            player1.player_hand.append(master_deck.pop())  # Dealing first card
            player1.player_hand.append(master_deck.pop())  # Dealing second card

            player1.player_score = player1.player_hand[0].value + player1.player_hand[1].value
            #  adding the values of the dealt cards to player score.

            # ***** Start of Blackjack-check block: *****
            face_cards = ["Jack", "Queen", "King"]
            ace = "Ace"
            ten = "10"
            face_count = 0  # counter variable to store face cards if in player hand.
            ace_count = 0  # counter variable to store aces if in player hand.
            ten_count = 0

            for card in player1.player_hand:  # for loop to iterate over the players initially dealt cards.
                if card.rank in face_cards:  # Checking if rank face cards are found in player hand.
                    face_count += 1  # if so, increment counter by 1
                if card.rank == ace:  # same for aces. Checking if rank ace in player hand and incrementing if so.
                    ace_count += 1  # incrementing ace count
                if card.rank == ten:
                    ten_count += 1

            if face_count == 1 and ace_count == 1:
                player1.bet += player1.bet * 3
                player1.chips += player1.bet
                print(f"{player1.player_hand} Blackjack! You win 2x your bet!")
                continue
            elif ace_count == 1 and ten_count == 1:
                player1.bet += player1.bet * 3
                player1.chips += player1.bet
                print(f"{player1.player_hand} Blackjack! You win 2x your bet!")
                continue
            else:
                print(f"Cards have been dealt. You have {player1.player_hand} with a value of "
                      f"{player1.player_score}")

            # ****** End of blackjack check ******

            # ***** Dealer gets dealt cards ******
            dealer.dealer_hand.append(master_deck.pop())  # Dealer gets first card.
            dealer.dealer_hand.append(master_deck.pop())  # Dealer gets second card.

            # Adding up dealer hand
            dealer.dealer_score = dealer.dealer_hand[0].value + dealer.dealer_hand[1].value

            print(f"The dealers visible card is {dealer.dealer_hand[0]} with a value of {dealer.dealer_hand[0].value}")
            # Easy access to both the dealers first card in the list, and its value. Since the card
            # is an instance (object) of the card class, it is stored in the list with all of its attributes.
            # This is a key principle in object-oriented programming, encapsulating data(the attributes) and
            # behaviour (methods) related to the object within a class. When creating instances of the class
            # it becomes very ease and intuitive to access and/or manipulate the attributes of the objects once
            # created.

            # Hit or stand decision for player:

        hit_or_stand = give_hit_or_stand_prompt()  # Extracted to give_hit_or_stand_prompt function.
        while hit_or_stand == 1:

            new_card = master_deck.pop()  # new_card variable used to store last card dealt.
            player1.player_hand.append(new_card)  # appending new card to player hand.
            player1.player_score += new_card.value  # Tallying score of hand so far.

            if player1.player_score <= 21:  # If player hits and score below 21.
                print(f"You chose to hit! You were dealt {new_card} with a value of "
                      f"{new_card.value}. Your hand now consists of {player1.player_hand} with "
                      f"a value of {player1.player_score}")
            elif player1.player_score > 21:
                print(f"Bust! You were dealt {new_card} with a value of {new_card.value} for a total score of"
                      f" {player1.player_score}.")

                # *** FIX TRY EXCEPT FOR WRONG INPUT ****
                play_again_or_not = input(f"Your money is gone..But hey, why not play again? "
                                          f"\n 1 - Play again \n 2 - Quit \n Make your choice:")
                play_or_not_decision = int(play_again_or_not)

                if play_or_not_decision == 1:
                    play_blackjack()
                else:
                    print("See you next time!")
                    exit(0)

            hit_or_stand = give_hit_or_stand_prompt()

        # ******* Dealer gets card ********

        draw_dealer_card = True

        while draw_dealer_card:
            if dealer.dealer_score == 21:  # Checking if dealer has BJ - THis works! Checked.
                draw_dealer_card = False  # stop dealing cards to dealer.
                print(f"Dealer has blackjack! {dealer.dealer_hand}. You lose. Better luck next time.")
            elif 17 <= dealer.dealer_score <= 21:  # If dealer has score between 17 and 21, stop dealing cards.
                draw_dealer_card = False
                print(f"Dealer stands! Dealer has {dealer.dealer_hand} with a value of {dealer.dealer_score}")
                check_winner()  # check winner function replaces block of if statement

            else:
                print(f"Dealer has to draw card at hand valued at 16. Dealer has {dealer.dealer_hand} "
                      f"with a value of {dealer.dealer_score}")
                dealer_new_card = master_deck.pop()  # Dealer draws new card
                dealer.dealer_hand.append(dealer_new_card)
                dealer.dealer_score += dealer_new_card.value
                print(f"Dealer draws {dealer_new_card}. Dealer hand now consists of {dealer.dealer_hand} with a"
                      f"value of {dealer.dealer_score}")

                if 17 <= dealer.dealer_score <= 21:  # Checked, this works. Dealer stands if true.
                    draw_dealer_card = False
                    print(f"Dealer stands! Dealer has {dealer.dealer_hand} with a value of {dealer.dealer_score}")
                    check_winner()  # check winner function replaces block of if statement

                elif dealer.dealer_score > 21:  # Checked - this works, prints dealer bust if bust.
                    draw_dealer_card = False
                    player1.bet += player1.bet * 2
                    player1.chips += player1.bet
                    print("Dealer bust! You win!")

        # Do you want to play again prompt - add wherever it is needed! fix this.


play_blackjack()
