# Lists

books_tolkien = ["The Hobbit", "Farmer Giles of Ham", "The Fellowship of the Ring",
                 "The Two Towers", "The Return of the King", "The Adventures of Tom Bombadil", "Tree and Leaf"]

print(books_tolkien[0:2])  # 1. Printer ut data fra indexpos. 0 til 2(ikke inkludert pos. 2)
print(books_tolkien[-2:])  # 1. Printer ut data fra indexpos. -2 og videre (fra slutten/den andre enden av listen)

books_tolkien.extend(["The Silmarillion", "Unfinished Tales"])  # 2. Append-funksjonen begrenset til 1 om gangen.

books_tolkien[0] = "Lord of the Rings: The Hobbit"  # 3.
books_tolkien[1] = "Lord of the Rings: Farmer Giles of Ham"  # 3.
books_tolkien[2] = "Lord of the Rings: The Fellowship of the Ring"  # 3.

books_tolkien.sort()
print(books_tolkien)



