courses = {"programming":
               {"instructor": "John",
                "students": ["Claire", "Ben", "Danny"]},
           "web development": {"instructor": "Gary",
                               "students": ["Lisa", "Jenny", "Jim"]}}

print(courses)

courses["database1"] = {"instructor": "Jimbo",
                        "students": ["Cathy", "Leonard", "David"]}
print(courses)

print(courses["programming"]["students"])
