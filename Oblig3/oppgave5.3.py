# Skrive/lese til fil
# 5.3 A

import json

movies_altered = [
    {"name": "Inception", "year": "2010", "rating": "8.7"},
    {"name": "Inside Out", "year": "2015", "rating": "8.1"},
    {"name": "Con Air", "year": "1997", "rating": "6.9"},
    {"name": "Killers of The Flower Moon", "year": "2023", "rating": "8.9"},
    {"name": "Interstellar", "year": "2014", "rating": "8.7"},
]

movies_to_json = [json.dumps(movie) for movie in movies_altered]  # Converting list of dict. to JSON.

reformatted_movies = [f"{json.loads(json_movie)['name']} - {json.loads(json_movie)['year']}, has a rating of "
                      f"{json.loads(json_movie)['rating']}. \n" for json_movie in movies_to_json]
# Loading from movies to json and reformatting using f-string to get desired output in text document when running funct.

# reformatted movies without json conversion:
# reformatted_movies = [f"{movie['name']} - {movie['year']}, has a rating of {movie['rating']}. \n"
# for movie in movies_altered] - This line works to, reformatting to a new list without JSON conversion.


def write_to_file(movie_list, file_name):
    with open(file_name, "w") as f:
        f.writelines(movie_list)


write_to_file(reformatted_movies, "movies.txt")

with open("movies.txt") as file1:
    content1 = file1.read()
print(content1)  # opening and reading file in terminal to see result here, too. 


# 5.3 B


def print_txt_file(file_name):
    with open(file_name) as file2:
        content2 = file2.read()
        print(content2)


print_txt_file("movies.txt")
