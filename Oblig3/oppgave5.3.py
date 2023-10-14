# Skrive/lese til fil

movies_altered = [
    {"name": "Inception", "year": "2010", "rating": "8.7"},
    {"name": "Inside Out", "year": "2015", "rating": "8.1"},
    {"name": "Con Air", "year": "1997", "rating": "6.9"},
    {"name": "Killers of The Flower Moon", "year": "2023", "rating": "8.9"},
    {"name": "Interstellar", "year": "2014", "rating": "8.7"},
]

reformatted_movies = [f"{movie['name']} - {movie['year']}, has a rating of {movie['rating']}. \n"
                      for movie in movies_altered]


def write_to_file(movie_list, file_name):
    with open(file_name, "w") as f:
        f.writelines(movie_list)


write_to_file(reformatted_movies, "movies.txt")

with open("movies.txt") as file1:
    content1 = file1.read()
print(content1)


def print_txt_file(file_name):
    with open(file_name) as file2:
        content2 = file2.read()
        print(content2)


print_txt_file("movies.txt")