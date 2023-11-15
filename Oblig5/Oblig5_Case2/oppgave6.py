import car_dealership as dealership
import oppgave3 as car_age_method


# Extracted code to method, to make it reusable as the task suggests.
def get_car_age_fee(car_age):
    if 0 <= car_age <= 3:
        return 6681
    elif 4 <= car_age <= 11:
        return 4034
    elif 12 <= car_age <= 29:
        return 1729
    return 0


def calculate_total_price(car_key):
    if car_key in dealership.car_register:
        car_price = dealership.car_register[car_key]["price"]
        car_age = car_age_method.get_car_age(car_key)  # importing get_car_age function from task 3.
        car_age_fee = 0

        if dealership.car_register[car_key]["new"]:
            car_age_fee = 10783
        else:
            car_age_fee = get_car_age_fee(car_age)

        total_car_price = car_price + car_age_fee

        return total_car_price


test_car = calculate_total_price("audiRS3")
print(test_car)
