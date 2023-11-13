
# Oppgaver:

# ***** HERE IS THE FUNCTION I NEED TO COMPLETE FOR TASK 1 *****
def print_ware_information(ware):


    # Prints info on a specified ware.

# ***** HERE IS THE FUNCTION I NEED TO COMPLETE FOR TASK 2
def calculate_average_ware_rating(ware):


    # Returns the average rating for a specified ware


# ***** HERE IS THE FUNCTION I NEED TO COMPLETE FOR TASK 3 *****
def get_all_wares_in_stock(all_wares):

    # Returns a dictionary with all wares in stock.

# ***** HERE IS THE FUNCTION I NEED TO COMPLETE FOR TASK 4 *****
def is_number_of_ware_in_stock(ware, number_of_ware):


    # Returns a boolean representing if a specified nr of a specific ware is in stock

# ***** HERE IS THE FUNCTION I NEED TO COMPLETE FOR TASK 5 *****
def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart,
number_of_ware):


    # Adds a specified number of a ware in a specified shopping cart


# ***** HERE IS THE FUNCTION I NEED TO COMPLETE FOR TASK 6*****
def calculate_shopping_cart_price(shopping_cart, all_wares, tax):

    # Returns price in shopping cart based on all wares in it.


def can_afford_shopping_cart(shopping_cart_price, wallet):

    # Returns a boolean based on if enough money in wallet


def buy_shopping_cart():

    # Buys goods in cart. Parameters defined in task.



# ***** Predefined functions: *****

def is_ware_in_stock(ware):
        # Returns a boolean that represents if a ware is in stock
    if ware["number_in_stock"] >= 1:
        return True
    else:
        return False


def clear_shopping_cart(shopping_cart):
        # Empties shopping cart
    shopping_cart.clear()



