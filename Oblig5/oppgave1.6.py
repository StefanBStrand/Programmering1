animals = ["honey badger", "giraffe", "ape", "zebra"]

animals[1] = "elephant"

animals.sort()

animals = animals[:2]

for animal in animals:
    print(animal)  # print will be ape and elephant

#  his line slices the animals list and keeps only the first two elements (elements at index 0 and index 1).
# The syntax [:2] means "start from the beginning of the list and go up to (but not including) the element at index 2".
# After this operation, animals will contain only the first two elements from the sorted list.

#  If instead, you used animals = animals[2:], this would mean "start from the element at index 2 @
#  and go all the way to the end of the list".
# This slice would include the elements from index 2 onwards.
# If your list was sorted alphabetically, then elements at index 2 and higher would be printed.
