import car_dealership as dealership

new_car_rent_fee = 1000


def rent_car_monthly_price(car):
    if car in dealership.car_register:
        car_price = dealership.car_register[car]["price"]
        monthly_rent = car_price * 0.033
        if dealership.car_register[car]["new"]:
            new_car_monthly_rent = monthly_rent + new_car_rent_fee
            return round(new_car_monthly_rent, 2)
        else:
            return round(monthly_rent, 2)
    else:
        print(f"{car} not in car register.")


monthly_rent_for_car = rent_car_monthly_price("audiRS3")
print(f"The price to rent this car is each month is {monthly_rent_for_car}.")


monthly_rent_for_car = rent_car_monthly_price("toyotaBZ4X")
print(f"The price to rent this car is each month is {monthly_rent_for_car}.")
