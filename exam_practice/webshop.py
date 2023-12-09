
# Oppgaver:

# ***** HERE IS THE FUNCTION I NEED TO COMPLETE FOR TASK 1 *****
def print_ware_information(ware):  # funct. takes. one parameter - ware
    print(f"Name: {ware['name']}"  # accessing the name (key) through the ware-varable 
          f"\nPrice: {ware['price']} ,-"
          f"\nNumber in stock: {ware['number_in_stock']}"
          f"\nDescription: {ware['description']}\n")

    # Prints info on a specified ware.

# ***** HERE IS THE FUNCTION I NEED TO COMPLETE FOR TASK 2


def calculate_average_ware_rating(ware):
    ratings = ware['ratings']  # assigning ware['ratings'] to variable ratings. ratings will take a new value for each
    # iteration in the for loop below.

    rating_sum = 0  # initializing a variable that will keep track og the total rating sum
    for rating in ratings:  # for loop that iterates over each value in the ratings key, whose value is a list
        rating_sum += rating  # adding each rating to the rating_sum

    try:  # code that can fail is wrapped in try/except block to catch possible zeroDivisionError if ratings list is
        # empty.
        return round(rating_sum / len(ratings), 1)  # calculation of avg rating for ware
    except ZeroDivisionError:
        return 0

    print()

    # Returns the average rating for a specified ware


# ***** HERE IS THE FUNCTION I NEED TO COMPLETE FOR TASK 3 *****


def get_all_wares_in_stock(all_wares):
    wares_in_stock = {}  # creating empty dictionary to add wares in stock to.
    for ware_id, ware in all_wares.items():  # iterating over the keys and values for all_wares dict.
        # .items() will return a view object (tuple) - in this case key = amd_processor etc, value is inner dict.
        if is_ware_in_stock(ware):  # predefined function returning a boolean used here. )
            wares_in_stock[ware_id] = ware  # setting/creating an entry using the ware_id (holding the names(keys)
            # of the wares and the values - the nested/inner dict (stored in ware-variable)

    return wares_in_stock  # returning dictionary where all wares in stock are added.
    # Returns a dictionary with all wares in stock.

# I now get why and how the predefined functions and variable names work in the whole setup
# of this oblig5. using the function is_ware_in_stock with ware-variable -- in this case passes the
# value inner dict and the function checks the key "number_in_stock" to get the value (check if it is >= 1



if __name__ == "__main__":

    # ***** HERE IS THE FUNCTION I NEED TO COMPLETE FOR TASK 4 *****
    def is_number_of_ware_in_stock(ware, number_of_ware):
        print()

        # Returns a boolean representing if a specified nr of a specific ware is in stock

    # ***** HERE IS THE FUNCTION I NEED TO COMPLETE FOR TASK 5 *****
    def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart,
    number_of_ware):
        print()

        # Adds a specified number of a ware in a specified shopping cart


    # ***** HERE IS THE FUNCTION I NEED TO COMPLETE FOR TASK 6*****
    def calculate_shopping_cart_price(shopping_cart, all_wares, tax):
        print()
        # Returns price in shopping cart based on all wares in it.


    def can_afford_shopping_cart(shopping_cart_price, wallet):
        print()
        # Returns a boolean based on if enough money in wallet


    def buy_shopping_cart():
        print()
        # Buys goods in cart. Parameters defined in task.


    # ***** Predefined functions: *****

    def is_ware_in_stock(ware):
        if ware["number_in_stock"] >= 1:
            return True
        else:
            return False


    def clear_shopping_cart(shopping_cart):
            # Empties shopping cart
        shopping_cart.clear()



