# Mer funksjoner

movies = [
    {"name": "Inception", "year": "2010", "rating": "8.7"},
    {"name": "Inside Out", "year": "2015", "rating": "8.1"},
    {"name": "Con Air", "year": "1997", "rating": "6.9"}
]


def print_movies():
    for movie in movies:
        print(f"{movie['name']}, {movie['year']}, has a rating of {movie['rating']}.")


print_movies()

# The Lion King - 1994 has a rating of 8.5 - Example printout.
# (f"{movies[0]['name']}, {movies[0]['year']} has a rating of {movies[0]['rating']}."))
