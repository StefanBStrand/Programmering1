courses = {"programming":
               {"instructor": "John",
                "students": ["Claire", "Ben", "Danny", "Blake"]},
           "web development": {"instructor": "Gary",
                               "students": ["Lisa", "Jenny", "Jim"]}}


def course_with_most_students(catalogue):
    max_students = 0
    course_name = ""

    for course, course_details in catalogue.items():
        student_count = len(course_details["students"])
        if student_count > max_students:
            max_students = student_count
            course_name = course

    return course_name


course_with_most_students(courses)

