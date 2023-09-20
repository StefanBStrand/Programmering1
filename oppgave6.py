import random

num_of_players = int(input("Enter number of players:"))

player_score = 0
throws = 0
total_score = []

for num in range(num_of_players):
    print(f"Player {num +1}")
    for darts in range(3):
        throws = (random.randrange(0, 60))
        print(throws)
        player_score += throws
        # player_score = score + throws. Not using the shorthand.
    total_score.append(player_score)
    player_score = 0

print(f"The total score is {total_score}")
