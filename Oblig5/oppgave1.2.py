# My answer before printing = [0, 1, 2, 3, 4]
# For range in 5 means: always starts at 0 and prints

numbers = []

for x in range(5):
    numbers.append(x)

print(numbers)

numbers1 = []

for y in range(5):
    numbers1.insert(y, 0)

# insert function used to insert an item at a specified index in a list.
# The insert method takes 2 arguments: the first arg is the index in the list where you want to insert your new item
# Second arg is what you want to insert into the list.

print(numbers1)  # Answer is: [0, 0, 0, 0, 0]

