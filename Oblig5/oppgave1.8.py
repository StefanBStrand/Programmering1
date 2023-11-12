shopping_list = {}


def add_item(item_name, quantity=1):
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity

    else:
        shopping_list[item_name] = quantity  # The syntax dictionary[key] = value is how you assign a value to
        # a key in a dictionary.

# When you see a line like shopping_list[item_name] = quantity in Python, it's essential to understand
# the relationship between keys and values in a dictionary. Here's a breakdown:
# The syntax dictionary[key] = value is how you assign a value to a key in a dictionary.

# shopping_list[item_name]
# Here, shopping_list is your dictionary, and item_name is the key you want to access or create.
# If item_name already exists in the dictionary, this expression refers to the value associated with that key.
# If item_name does not exist, this expression creates a new key in the dictionary with the name item_name.

# = quantity
# This part assigns the value of quantity to the key item_name in the dictionary.
# f the key is new (just created), it simply sets its value to quantity.
# If the key already existed (which in this case, it wouldn't, because we are in the else block),
# it would overwrite the existing value with the new value quantity.


add_item("Bread", 2)
add_item("Milk")
add_item("Milk", 2)
add_item("Bread", 2)
add_item("Eggs")


print(shopping_list)


# 1: list is Bread: 2
# 2 Bread: 2, Milk: 1
# 3 Bread: 2, Milk: 3
# 4 Bread: 4, Milk: 3
# 5 Bread: 4, Milk: 3, Eggs: 1
