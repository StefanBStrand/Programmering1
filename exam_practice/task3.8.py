courses = {"programming":
               {"instructor": "John",
                "students": ["Claire", "Ben", "Danny"]},
           "web development": {"instructor": "Gary",
                               "students": ["Lisa", "Jenny", "Jim"]}}


def find_instructor(catalogue, course_name):
    if course_name in catalogue:
        return print(catalogue[course_name]["instructor"])  # FYI PRINT returns None, should not be used with return.


find_instructor(courses, "web development")
