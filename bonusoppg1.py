#  Bonusoppgave 1 - Dart 2.0

import random

num_of_players = int(input("Enter number of players:"))
num_of_darts = int(input("Enter number of darts:"))
num_of_rounds = int(input("Enter number of rounds:"))

player_score = 0
throws = 0
total_score = []


for num in range(num_of_players):
    print(f"Player {num +1}")
    for darts in range(num_of_darts):
        for rounds in range(num_of_rounds):
            throws = (random.randrange(0, 60))
        print(throws)
        player_score += throws

    total_score.append(player_score)
    player_score = 0

print(f"The total score is {total_score}")
