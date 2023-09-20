import random

num_of_players = int(input("Enter number of players:"))

player_score = 0
for num in range(num_of_players):
    for darts in range(3):
        throws = (random.randrange(0, 60))
        print(throws)
        player_score += throws  # score = score + throws. Not using the shorthand.

print(f"The total score is {player_score}")
