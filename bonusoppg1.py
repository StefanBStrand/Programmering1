#  Bonusoppgave 1 - Dart 2.0

import random

num_of_players = int(input("Enter number of players:"))
num_of_darts = int(input("Enter number of darts:"))
num_of_rounds = int(input("Enter number of rounds:"))

player_score = 0

#  dart_scores = [i for i in range(1, 21)] + [2*i for i in range(1, 21)] + [3*i for i in range(1,21)] + [0, 25, 50]
dart_smores = []

for i in range(1, 21):
    dart_smores.append(i)
    dart_smores.append(2*i)
    dart_smores.append(3*i)

dart_smores.append(0)
dart_smores.append(25)
dart_smores.append(50)


total_score = []

for num in range(num_of_players):
    print(f"**Player {num +1}**")
    for rounds in range(num_of_rounds):
        print(f"Round {rounds +1}")
        for throws in range(num_of_darts):
            score = random.choice(dart_smores)
            print(score)
            player_score += score
    total_score.append(player_score)
    player_score = 0

print(f"The total score is {total_score}")

#  Change name of list used to be dart_scores.
#  Clean up code.