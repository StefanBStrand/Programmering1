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
    def is_number_of_ware_in_stock(ware, number_of_wares):
        return number_of_wares <= ware['number_in_stock']


    #  ware-variable represents a ware in all_wares, e.g. "amd_processor"
    #  number_of_wares represents the desired number we want to check
    #  if is in stock. return number_of_wares <= ware['number_in_stock']
    #  - this line returns a boolean based
    #  on the check/comparison performed here --
    #  if number_of_wares (quantity) is less than or equal to
    #  the stock - which is ware['number_in_stock']
    #  it returns True - indicating sufficient stock
    #  otherwise returns False.

    # Returns a boolean representing if a specified nr of a specific ware is in stock

    # ***** HERE IS THE FUNCTION I NEED TO COMPLETE FOR TASK 5 *****


    def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart,
                                            number_of_wares=1):

        if is_number_of_ware_in_stock(ware, number_of_wares):  # re-using function is_number_of_ware_in_stock to check
            shopping_cart[ware_key] = number_of_wares  # if numofware in stock -> add/create entry in dict shopping_cart
            print(f"{number_of_wares} instance(s) of {ware['name']} was added to shopping cart.")
            # this whole block checks if the desired num of wares is in stock - if True - adds to cart
        elif is_ware_in_stock(ware):  # re-using predefined function to check if ware in stock
            number_of_wares = ware[number_of_wares]  # sets number of wares based on as many as in stock
            shopping_cart[ware_key] = number_of_wares  # adds amount of wares to shopping cart.
            print(f"There was just {number_of_wares} in stock")
            print(f"{number_of_wares} instance(s) of {ware['name']} added to shopping cart.")
        else:
            print(f"{ware['name1']} is not in stock")


    # Adds a specified number of a ware in a specified shopping cart

    # ***** HERE IS THE FUNCTION I NEED TO COMPLETE FOR TASK 6*****
    def calculate_shopping_cart_price(shopping_cart, all_wares, tax=1.25):
        total_price = 0
        for ware_id, number_of_wares in shopping_cart.items():
            total_price += all_wares[ware_id]['price'] * tax * number_of_wares

        return total_price

    # Returns price in shopping cart based on all wares in it.
    # total_price = 0 -> initializes a variable to keep track of total_price
    # for loop -> ware_id stores e.g. amd_processor, number_of_wares
    # stores number_of_wares in shopping cart (values of the ware_id key)

    # keep in mind that the shopping-cart dictionary
    # does NOT have a nested dictionary and structure
    # is a single dict with key (ware_id) and value(quantity)
    # which is stored in number_of_wares variable

    def can_afford_shopping_cart(shopping_cart_price, wallet):
        return shopping_cart_price < wallet.get_amount()
        # Returns a boolean based on if enough money in wallet


    def buy_shopping_cart(shopping_cart, all_wares, wallet):
        for ware_id, number_of_wares in shopping_cart.items(): #iterating over key/value pairs in shopping cart
            ware = all_wares[ware_id]  # setting variable ware to be ware_id (which is the key in shopping cart
            if is_number_of_ware_in_stock(ware, number_of_wares):  # reusing funct. isnumofware in stock here.
                #  code block executes if return value is True! (there is enough ware in stock).
                print(f"Purchasing {number_of_wares} of {ware['name']}")
                ware['number_in_stock'] -= number_of_wares  # subtracting number in stock value with numberOfWares
                # BLOCK OF CODE ABOVE: checks if desired quantity of wares for purchase are in stock, then purchases.
            elif is_ware_in_stock(ware):  # this code block runs if expression is True
                print(f"Sorry, there was only {number_of_wares} of {ware['name']} available. Amount is now in cart")
                shopping_cart[ware_id] = ware['number_in_stock']  # setting shopping cart key's value to
                # amount of wares in stock! THIS is how it looks when setting/Creating/updating a key and value!
                # ware holds all_wares[ware_id].
                ware['number_in_stock'] = 0
            else:
                print(f"Sorry, {ware['name']} is not out of stock")
                remove_ware_from_shopping_cart(ware_id, shopping_cart)  # using predefined function to remove

        shopping_cart_price = calculate_shopping_cart_price(shopping_cart, all_wares)  # using predefined funct.
        print(f"The total price will be {shopping_cart_price}")

        if can_afford_shopping_cart(shopping_cart_price, wallet):
            wallet.subtract_amount(shopping_cart_price)  # using instance wallet of class Wallet and defined method.
            print("Transaction finished. Wares bought: ")
            print(shopping_cart)
            clear_shopping_cart(shopping_cart)
        else:
            print(shopping_cart)
            print("Sorry. You cannot afford the price of this shopping cart")




    # ***** Predefined functions: *****


    def remove_ware_from_shopping_cart(ware_id, shopping_cart):
        if ware_id in shopping_cart:
            del shopping_cart[ware_id]  # removes key AND value!


    def is_ware_in_stock(ware):
        if ware["number_in_stock"] >= 1:
            return True
        else:
            return False


    def clear_shopping_cart(shopping_cart):
        # Empties shopping cart
        shopping_cart.clear()
