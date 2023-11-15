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


shopping_cart_2 = {}

# Reusing function from case1 - task5 in this one. Just need to add calculate price function and rename some things.


def calculate_shopping_cart_price(ware, shopping_cart_key, shopping_cart, stock_holdings, number_of_ware=1,
                                  add_tax=True):

    # Adding ware to the shopping cart
    if ware in stock_holdings:
        in_stock = stock_holdings[ware]["number_in_stock"]

        if in_stock == 0:
            print(f"{ware} is not in stock, you cannot buy this ware at the moment")
            return

        amount_to_add_to_cart = min(number_of_ware, in_stock)

        if shopping_cart_key in shopping_cart:
            shopping_cart[shopping_cart_key]["quantity"] += amount_to_add_to_cart
        else:
            shopping_cart[shopping_cart_key] = {
                "name": stock_holdings[ware]["name"],
                "price": stock_holdings[ware]["price"],
                "quantity": amount_to_add_to_cart
            }

        stock_holdings[ware]["number_in_stock"] -= amount_to_add_to_cart
        print(f"Added {amount_to_add_to_cart} of {ware} to your shopping cart.")
        print()
    else:
        print(f"{ware} is not available to buy.")
        return

    # calculating price and adding tax to cart here:
    # iterating over each key in shopping cart, multiplying price * quant to get total price

    total_price = 0

    for key in shopping_cart:
        item_price = shopping_cart[key]["price"]
        item_quantity = shopping_cart[key]["quantity"]
        total_price += item_price * item_quantity

    if add_tax:
        tax_rate = 0.25
        total_price *= (1 + tax_rate)

    print(f"Total price of the shopping cart (including tax): {round(total_price, 1)}")


calculate_shopping_cart_price("amd_processor", "amd_processor_key", shopping_cart_2, all_wares,
                              7, True)
print()
print(all_wares["amd_processor"]["number_in_stock"])
