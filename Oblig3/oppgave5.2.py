# Mer funksjoner
# 5.2 A

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

# 5.2 B


def avg_movie_rating():
    total_rating = 0  # initializing a variable for the total rating to be stored.
    for movie in movies:  # for loop to loop through all the movie ratings in the list
        total_rating += float(movie["rating"])  # adding up the converted ratings to total_rating.
    return round(total_rating / len(movies), 1)  # rounding the answer down to 1 decimal, for consistency reasons.

# Remember to place return statement outside the loop. If not, it terminates after the first iteration.
         

print(f"The average movie rating is: {avg_movie_rating()}")

#  return float(movie['rating']) / len(movies)
