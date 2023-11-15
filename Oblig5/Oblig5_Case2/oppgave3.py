import car_dealership as dealership
import datetime


def get_car_age(car_key):
    if car_key in dealership.car_register:
        car = dealership.car_register[car_key]
        car_manufacture_date = datetime.date(car["year"], 1, 1)  # Using the 1st day of the month

        # Get today's date
        today = datetime.date.today()

        # Calculate the age
        age_years = today.year - car_manufacture_date.year

        return age_years
    else:
        return "Car not found in the register"


age_of_toyota = get_car_age("toyotaBZ4X")

print(f"The age of the car is {age_of_toyota} years old")

