#  5.1 Dict og funksjoner
#  5.1 A:

movies = [
    {"name": "Inception", "year": "2010", "rating": "8.7"},
    {"name": "Inside Out", "year": "2015", "rating": "8.1"},
    {"name": "Con Air", "year": "1997", "rating": "6.9"}
]

# 5.1 B:


def add_movie(movie_list, name, year, rating="5.0"):  # default value set for rating if val. not passed.
    new_movie = {"name": name,
                 "year": year,
                 "rating": rating
                 }
    movie_list.append(new_movie)


add_movie(movies, "Grease", "1978", "7.2")
add_movie(movies, "Ocean's Eleven", "2001", "7.7")
add_movie(movies, "Catch me if you can", "2002", "8.1")
add_movie(movies, "Good Will Hunting", "1997")  # No value for rating passed in - default value applies.

print(movies)
