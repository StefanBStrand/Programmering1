all_wares = {
    "amd_processor": {
        "name": "AMD Ryzen 9 5900X Processor",
        "price": 5590.0,
        "number_in_stock": 50,
        "ratings": [4.5, 4.0, 5.0, 5.0, 4.5, 3.0],
        "description": "All the cores and threads you'll need"
    },

    "playstation_5": {
        "name": "PlayStation 5",
        "price": 5999.0,
        "number_in_stock": 0,
        "ratings": [5.0, 5.0, 4.5, 2.0, 5.0, 4.5, 4.0],
        "description": "Next generation console, never in stock"
    },
    "hdmi_cable": {
        "name": "Belkin Ultra High Speed HDMI Cable - 2m",
        "price": 349.0,
        "number_in_stock": 3,
        "ratings": [5.0, 5.0, 4.5, 5.0, 5.0, 5.0],
        "description": "A high speed overprices HDMI cable!",
    }
}

shopping_cart1 = {}

# First check if ware is in all_wares
# if it is, then check the stock of ware
# If stock is zero, --> print you cannot add this item or something that way.

# If stock not zero, add specified amount (number of ware) to shopping_cart
# if specified amount is more than stock --> add entire stock of ware or ware_key (If i set this to be stock or so.
# add correct way of ware to be added to the dictionary shopping cart.
# Remember to deduct amount added to cart from stock in all_wares.

# changed ware_key to shopping_cart_key. The name ware_key of variable before confused me.


def add_number_of_ware_to_shopping_cart(ware, shopping_cart_key, shopping_cart, number_of_ware=1):
    if ware in all_wares:
        in_stock = all_wares[ware]["number_in_stock"]  # creating variable for simplicity.

        if in_stock == 0:
            print(f"{ware} is not in stock, you cannot buy this ware at the moment")
            print("Add something that is in stock to your cart.")
            print("This is our current stock:")
            print()
            for item in all_wares:
                if all_wares[item]["number_in_stock"] > 0:
                    print(item)
            return

        amount_to_add_to_cart = min(number_of_ware, in_stock)  # min function used to find the smallest of two arguments
        # easy way to check if I want to add more than what is available in stock. If so, the min (smaller number) of
        # the two will be returned.

        if shopping_cart_key in shopping_cart:  # checking to see if ware already exists as key in shopping cart.
            shopping_cart[shopping_cart_key]["quantity"] += amount_to_add_to_cart
        else:  # Creating a new entry in dictionary if key is not found there from before.
            shopping_cart[shopping_cart_key] = {
                "name": all_wares[ware]["name"],
                "price": all_wares[ware]["price"],
                "quantity": amount_to_add_to_cart
            }

        all_wares[ware]["number_in_stock"] -= amount_to_add_to_cart

        print(f"Added {amount_to_add_to_cart} of {ware} to your shopping cart.")
    else:
        print(f"{ware} is not available to buy.")


add_number_of_ware_to_shopping_cart("playstation_5", "playstation_5", shopping_cart1,
                                    4)
print()
add_number_of_ware_to_shopping_cart("amd_processor", "amd_processor", shopping_cart1,
                                    5)
print()
print(all_wares["amd_processor"]["number_in_stock"]) # checking to see if deducting from stock in all_wares.
