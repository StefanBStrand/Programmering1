book_prices = {"Donald Duck": 135.5,
               "Beauty & Beast": 169.9,
               "Snow White": 199.9}


def print_book_price(books, title):
    if title in books:
        print(books[title])
    else:
        print("Book not found")


print_book_price(book_prices, "Donald Duck")
print_book_price(book_prices, "Batman")


