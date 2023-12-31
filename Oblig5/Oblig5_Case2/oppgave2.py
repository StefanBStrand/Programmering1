import car_dealership as dealership


def create_car(car_key, brand, model, price, year, month, new, km):
    if car_key in dealership.car_register:

        car = dealership.car_register[car_key]
        # Option to update car info if car exists in register:
        car["brand"] = brand
        car["model"] = model
        car["price"] = price
        car["year"] = year
        car["month"] = month
        car["new"] = new
        car["km"] = km
    else:  # If car does not already exist, create new entry.
        dealership.car_register[car_key] = {
            "brand": brand,
            "model": model,
            "price": price,
            "year": year,
            "month": month,
            "new": new,
            "km": km
        }

    for key, value in dealership.car_register.items():
        print(f"{key}")
        print()  # empty print statements for improved readability when printing function.
        for item, item_details in value.items():
            print(f"{item_details}")
        print()


create_car("audi", "audi", "S8", 1000000, 2020, 8, False, 25000)
