# For-loops Dart

import random

num_of_players = input("Enter number of players:")

score = 0
for i in range(3):
    throws = (random.randrange(0, 60))
    print(throws)
    score += throws  # score = score + throws. Not using the shorthand.

print(f"The total score is {score}")





