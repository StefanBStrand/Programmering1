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
        print(f"The average rating for {ware} is {avg_rating}")


calculate_average_ware_rating("amd_processor")




#  print(f"Average rating for the AMD Processor:{ws.calculate_average_ware_rating(all_wares['amd_processor'])}")