animals_in_zoo = {"honey badger": 2, "ape": 15, "zebra": 6, "giraffe": 4}  # creating a dictionary with zoo animals

for animal in animals_in_zoo:
    if animals_in_zoo[animal] < 5:
        print(animal.title())

# Answer here is that it prints out Honey Badger and Giraffe.

#  if animals_in_zoo[animal] < 5:
#  In this line, you're checking if the value associated with the current animal key in the dictionary is less than 5.
#  This is effectively checking if there are less than 5 animals of that type in the zoo.

# The square brackets [] are used to access an element of a dictionary by its key.
# animal is a string (the name of an animal from the dictionary).

# .title() is a string method in Python. It's not a keyword, but a method that formats a string to 'title case'.
# In title case, the first letter of each word is capitalized, and all other letters are lowercase.
# So, animal.title() takes the name of the animal and converts it to title case.
# For example, if animal is "honey badger", animal.title() will be "Honey Badger".
