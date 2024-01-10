courses = {"programming":
               {"instructor": "John",
                "students": ["Claire", "Ben", "Danny"]},
           "web development": {"instructor": "Gary",
                               "students": ["Lisa", "Jenny", "Jim"]}}

# ANOTHER EXAMPLE OF FUNCTION FROM TASK 3.8 - but BETTER,with tips from GPT:


def find_instructor(catalogue, course_name):
    if course_name in catalogue:
        instructor = catalogue[course_name]["instructor"]
        print(instructor)
        return instructor
    else:
        print("Course not found")
        return None
