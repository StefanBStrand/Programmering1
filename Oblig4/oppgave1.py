# Oppgave 1 - Klasser og objekter
# A:

class Movies:
    def __init__(self, title, year, score):  # init method with attributes title, year and score
        self.title = title
        self.year = year
        self.score = score
        #  a method is a function that is associated with an object.

    def movie_info(self):
        return f"{self.title} - was released in {self.year} and currently has a score of {self.score}."


movie1 = Movies("Inception", 2008, 8.8)
movie2 = Movies("The Martian", 2015, 8.0)
movie3 = Movies("Joker", 2019, 8.4)

print(f"{movie1.title} was released in {movie1.year} and currently has a score of {movie1.score}.")
print(f"{movie2.title} was released in {movie2.year} and currently has a score of {movie2.score}.")
print(f"{movie3.title} was released in {movie3.year} and currently has a score of {movie3.score}.")

print(movie1.movie_info())
print(movie2.movie_info())
print(movie3.movie_info())

# title, year and score are both attributes of the Movies class and parameters of the init method.
# an attribute is a variable associated with an instance, or class. It represents some kind of state or
# data for the object. Accessible via dot notation. A parameter on the other hand is a named entity
# in the function/method definition. When a method/function is called, you provide values for these parameters,
# and these values are referred to as arguments.
