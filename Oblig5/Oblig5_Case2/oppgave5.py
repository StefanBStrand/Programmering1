import datetime
import car_dealership as dealership


def next_eu_control(car_key):
    if car_key in dealership.car_register:
        car = dealership.car_register[car_key]
        car_manufacture_year = car["year"]
        car_manufacture_month = car["month"]

        # Get the current date.
        today = datetime.date.today()

        # adding 2 years from manufacture date until the date is in the future for the new inspection.
        next_inspection_year = car_manufacture_year
        while next_inspection_year <= today.year:
            next_inspection_year += 2

        next_inspection_date = datetime.date(next_inspection_year, car_manufacture_month, 1)
        # Creating a date object from the datetime module, using the date class of that module. This is now
        # stored in the variable next inspection date.

        return next_inspection_date
    else:
        print("Car is not in car register")


test_car = next_eu_control("audiRS3")
print(f"The next inspection date for your car is {test_car}.")
