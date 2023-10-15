#  Dictionaries

student = {
    "first_name": "Ola",
    "last_name": "Nordmann",
    "favourite_course": "Programmering 1"
}

#  1:
print(f"First name and last name: {student['first_name']} {student['last_name']}")

#  2:
student["favourite_course"] = "Programmering 1, ITF10219"
print(student["favourite_course"])  # Print to check result.

#  3:
student["age"] = 35

print(student)  # Printing to check result.
