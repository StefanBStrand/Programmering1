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


def calculate_average_ware_rating(ware):
    if ware in all_wares:
        total_rating = sum(all_wares[ware]["ratings"])
        ratings_length = len(all_wares[ware]["ratings"])
        avg_rating = total_rating / ratings_length
        print(f"The average rating for {ware} is {round(avg_rating, 1)}")
    else:
        print("Selected ware not in stock or not available. This is the current stock:")
        print()  # this adds a blank line for separation and readability.
        all_wares_in_stock = all_wares.items()  # all_wares_in_stock is now a tuple with first element is the key, like
        # amd_processor, and the second element is the value (in this case the dictionary with details of that ware.

        for item, item_details in all_wares_in_stock:  # the for loop iterates and for each iteration, item variable
            # stores the key, like amd_processor, and the item_details stores the nested dict with details
            print(f"{item}:")  # printing out the item, e.g. amd_processor, first, like a heading.
            for item_key, item_value in item_details.items():  # here, item_key holds the key in the details of the
                # inner dictionary, like "name", "price", etc. item_value holds the value to the keys.
                print(f" {item_key}: {item_value}")  # here, keys and values for inner (nested) dict is printed
            print()  # another blank line for readability
        

calculate_average_ware_rating("xbox")
