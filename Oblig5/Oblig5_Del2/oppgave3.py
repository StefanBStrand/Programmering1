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


def get_all_wares_in_stock(ware):
    if ware in all_wares:  # Checking to see if ware is in all_wares (is ware a key in all_wares)
        if all_wares[ware]["number_in_stock"] > 0:  # If ware is in all_wares, checking if in stock
            print(f"{ware} is in stock. Here are the details:")  # If ware is in stock, print details for ware
            print()
            for item_key, item_value in all_wares[ware].items():  # .items for getting key/value pairs in ware
                print(f"{item_key}: {item_value}")

        else:
            print(f"{ware} is not in stock.")
    else:
        print(f"{ware} is not available!")
        print("Here is what we have available:")
        print()
        for item, item_details in all_wares.items():  # item stores key, e.g., amd_processor, item_details stores
            # key/value pairs of amd_processors' details.
            if item_details["number_in_stock"] > 0:  # again checking if we have it ins stock. If so, print. 
                print(f"{item}")


get_all_wares_in_stock("xbox")
