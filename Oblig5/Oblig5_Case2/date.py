import datetime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.date = datetime.date(self.year, self.month, self.day)

