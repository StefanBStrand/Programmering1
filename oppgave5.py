# For-loops Dart

import random

score = 0
for i in range(3):
    throws = (random.randrange(0, 60))
    print(throws)
    score += throws  # score = score + throws. Not using the shorthand.

print(f"The total score is {score}")





