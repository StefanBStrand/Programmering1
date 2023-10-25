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


deck_of_cards = {}  # deck of cards being a dictionary might be better?
prompts = []
player_hand = []
dealer_hand = []

playing = True


def play_blackjack():
    while playing:
        Dealer.dealer_score = 0
        Player.player_score = 0
        Player.chips = 3000
