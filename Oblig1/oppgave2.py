first_name = "Stefan"
last_name = "Strand"
age = str(35)  # Using the str function to convert the number to a string,
# so it can be printed out in the result variable.

result = "Hei. Jeg heter " + first_name + " " + last_name + " og er " + age + " år gammel."
print(result)

#  Change after feedback on oblig 1: Use f-strings! See below:

result = f"Hei. Jeg heter {first_name} {last_name} og er {age} år gammel."
print(result)
# f-strings: is a formatted string literal that allows you to embed expressions inside string literals.
# Has to be prefixed with "f" or "F". Introduced in python 3.6. Variables and expressions can be
# embedded straight into strings using surrounding curly brackets.
