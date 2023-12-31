# Iterating through a list, for-loop.

lord_of_the_rings = []

books_tolkien = ['Lord of the Rings: Farmer Giles of Ham', 'Lord of the Rings: The Fellowship of the Ring',
'Lord of the Rings: The Hobbit', 'The Adventures of Tom Bombadil', 'The Return of the King', 'The Silmarillion',
'The Two Towers', 'Tree and Leaf', 'Unfinished Tales']

for books in books_tolkien[0:3]:  # Making a variable called "books", which stores books_tolkien index 0:3 in this case.
    lord_of_the_rings.append(books)  # Using the append function to add the desired books to the empty list.
    # If extend method is used, it iterates through every letter in the name of the books/elements,
    # Since a string is an iterable. Extend expects an iterable as an argument.

print(lord_of_the_rings)  # if print statement is put inside the for loop, it prints as an iteration.

lord_of_the_rings = []  # If list is not reset at this point, then print statement second time around doubles
# the amount of books printed.

for books in books_tolkien:
    if "Lord of the Rings" in books:
        lord_of_the_rings.append(books)

print(lord_of_the_rings)
