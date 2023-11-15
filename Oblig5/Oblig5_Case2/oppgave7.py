class Car:
    def __init__(self, brand, model, price, year, month, new, km):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.new = new
        self.km = km


    def print_car_information(self):  # this one could come in handy when wanting an easy and readable friendly
        print() # way of printing the car info. When trying to print objects created from classes, if the
        # __str__ method is not defined in the object, it will print a very not-human friendly display
        # of the object.

    def get_car_age(self):  # This method could be used when dealing with car age and specific dates which is
        print()  # handled by the method. No need to import datetime in other files where you might need to
        # know the age of the car.

    def get_car_monthly_price(self):  # This is very usable if renting the car is an option for the business.
        print()

    def next_eu_control(self):  # This is equally handy when wanting to check the next inspection date for a selected
        print()  # car

    def calculate_total_price(self):  # Again, easy way to get the total price of various cars based on their age
        print()
