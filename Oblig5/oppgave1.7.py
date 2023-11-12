# gorilla, dog, dodo, cat, alligator

animals = ["Elephant", "Dog", "Cat", "Gorilla", "Dodo"]

animals = animals[1:3]  # slices list and only takes with it items from index 1 to index 2 (not including 3)
#  List now consists of only dog and cat, meaning the new list has 2 index positions, index 0 and 1.

animals[0] = "Alligator"
# Dog becomes Alligator

animals.sort(reverse=True)
# Alligator and cat becomes Cat and alligator

print(animals)  # prints cat and alligator

# animals = animals[1:3]
# This line slices the animals list to include only the elements from
# index 1 to index 2 (slicing is exclusive of the ending index).

# The slice animals[1:3] results in ["Dog", "Cat"], so now animals contains just these two elements.
# animals.sort(reverse=True) This line sorts the animals list in reverse alphabetical order.
# After sorting, the list ["Alligator", "Cat"] becomes ["Cat", "Alligator"], because "Cat" comes after "Alligator"
# in reverse alphabetical order.
