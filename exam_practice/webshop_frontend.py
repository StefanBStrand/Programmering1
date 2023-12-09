import webshop as ws  # imports file webshop as variable ws
from wallet import Wallet  # From file wallet import Class Wallet is what this does.

all_wares = {
    "amd_processor": {
        "name": "AMD Ryzen 9 5900X Processor",
        "price": 5590.0,
        "number_in_stock": 50,
        "ratings": [4.5, 4.0, 5.0, 5.0, 4.5, 3.0],
        "description": "All the cores and threads you'll need!",
    },

    "playstation_5": {
        "name": "PlayStation 5",
        "price": 5999.0,
        "number_in_stock": 0,
        "ratings": [5.0, 5.0, 4.5, 2.0, 5.0, 4.5, 4.0],
        "description": "Next generation console, never in stock!",
    },
    "hdmi_cable": {
        "name": "Belkin Ultra High Speed HDMI Cable - 2m",
        "price": 349.0,
        "number_in_stock": 3,
        "ratings": [5.0, 5.0, 4.5, 5.0, 5.0, 5.0],
        "description": "A high speed overprices HDMI cable!",
    }
}

# Filters out all wares that are in stock and prints info about each of them

if __name__ == "__main__":

    all_wares_in_stock = ws.get_all_wares_in_stock(all_wares)

    for ware in all_wares_in_stock.values():
        ws.print_ware_information(ware)

    # Prints average rating for this ware

    print(f"Average rating for the AMD Processor:{ws.calculate_average_ware_rating(all_wares['amd_processor'])}")
    print()

    # Creates empty shopping cart

    shopping_cart = {}

    ws.add_number_of_ware_to_shopping_cart("amd_processor",
                                           all_wares["amd_processor"], shopping_cart)
    ws.add_number_of_ware_to_shopping_cart("playstation_5",
                                           all_wares["playstation_5"], shopping_cart, 2)
    ws.add_number_of_ware_to_shopping_cart("hdmi_cable", all_wares["hdmi_cable"],
                                           shopping_cart, 4)

    print()
    print(f"THe shopping cart: {shopping_cart}")

    # Creating instance of class Wallet: a wallet containing 10000 NOK
    wallet = Wallet(10000)

    # Tries to buy wares in shopping cart
    ws.buy_shopping_cart()  # parameters defined in task will go inside partentheses


    # Prints amount of money in wallet after purchase
    print(f"The amount in the wallet after the purchase: {wallet.get_amount()}")
