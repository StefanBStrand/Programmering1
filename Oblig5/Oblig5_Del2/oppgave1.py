

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


def print_ware_information(ware_name):  # function taking one parameter.
    if ware_name in all_wares:  # Checking to see if name of ware is in dict all_wares, storing it in ware_name
        for key, value in all_wares[ware_name].items(): # .items used with dict. Returns object with key-value pairs.
            print(f"{key}: {value}")
    else:
        print("Name: Example Ware")
        print("Price: 3999,-")
        print("Number in stock: 30")
        print("Description: A non-existent ware used only for this example")


print_ware_information("amd_processor")
print_ware_information("Xbox")

