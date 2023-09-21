# For-loops Dart

import random

total_score = 0
for i in range(3):
    score = (random.randrange(0, 60))
    print(score)
    total_score += score

print(f"The total score is {total_score}")
