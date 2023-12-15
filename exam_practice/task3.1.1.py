# Alternative solution to 3.1 using the for loop i wrote on the exam.. which was not great.

menu = {"Ribbe": 129.90,
        "Pinnekjøtt": 159.90,
        "Lutefisk": 148.90,
        "Reinsdyrstek": 190.90}


def print_meal(menu, menu_item):  # do not shadow menu variable here from outer scope, in this case the dict.
    for item, price in menu.items():
        if item == menu_item:
            print(f"{item} - {price}")
            break
    else:
        print("Item not found in the menu.")


print_meal(menu, "Ribbe")
