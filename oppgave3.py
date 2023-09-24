# Lists

books_tolkien = ["The Hobbit", "Farmer Giles of Ham", "The Fellowship of the Ring",
                 "The Two Towers", "The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf"]

print(books_tolkien[0:2])  # 1. Prints data from indexpos. 0 to 2(not including pos. 2)
print(books_tolkien[-2:])  # 1. Prints out data from indexpos. -2 and thereafter (fom the back of the list.)

books_tolkien.extend(["The Silmarillion", "Unfinished Tales"])  # 2. Append-function limited to appending 1 at a time.

books_tolkien[0] = "Lord of the Rings: The Hobbit"  # 3.
books_tolkien[1] = "Lord of the Rings: Farmer Giles of Ham"  # 3.
books_tolkien[2] = "Lord of the Rings: The Fellowship of the Ring"  # 3.

books_tolkien.sort()
print(books_tolkien)
