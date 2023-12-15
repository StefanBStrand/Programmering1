# Task 3.1 eksamen Prog 1 - December 23

menu = {"Ribbe": 129.90,
        "Pinnekjøtt": 159.90,
        "Lutefisk": 148.90,
        "Reinsdyrstek": 190.90}


def print_meal(christmas_menu, menu_item):
    if menu_item in christmas_menu:
        print(f"{menu_item} - {christmas_menu[menu_item]}")


print_meal(menu, "Lutefisk")


# In my answer on the exam I used a for loop to iterate over the menu.items..