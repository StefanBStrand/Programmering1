import car_dealership as dealership


def print_car_information(car):
    if car in dealership.car_register:
        for key, value in dealership.car_register[car].items():
            print(f"{key}: {value}")
    else:
        print("Car not found")


print_car_information("toyotaBZ4X")
