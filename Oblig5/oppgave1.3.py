class Course:
    def __init__(self, name, number_of_students, study_points=10):
        self.name = name
        self.number_of_students = number_of_students
        self.study_points = study_points

    def get_description(self):
        return f"The course {self.name} has {self.number_of_students} students" \
               f" and {self.study_points} study points."


programmering_1 = Course("Programmering 1", 215)
programmering_2 = Course("Programmering 2", 100, 20)

print(programmering_1.get_description())
print(programmering_2.get_description())

#  in OOP (object-oriented programming) objects are instances of classes. A class is like a blueprint,
#  and an object is an actual entity created based on that blueprint.

# A method is a function that is defined inside a class and is meant to be called on
# instances of that class, that is, Objects.
# The syntax for calling a method on an object can be described with the example:
# print(programmering_1.get_description())
