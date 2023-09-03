num1 = input("Enter a number:")
num2 = input("Enter another number:")

result = float(num1) * float(num2)
print(str(num1) + " * " + str(num2) + " = " + str(result))

result = float(num1) / float(num2)
print(str(num1) + " / " + str(num2) + " = " + str(result))

result = float(num1) + float(num2)
print(str(num1) + " + " + str(num2) + " = " + str(result))

result = float(num1) - float(num2)
print(str(num1) + " - " + str(num2) + " = " + str(result))

result = float(num1) % float(num2)
print(str(num1) + " % " + str(num2) + " = " + str(result))

result = float(num1) ** float(num2)
print(str(num1) + " ** " + str(num2) + " = " + str(result))

result = float(num1) // float(num2)
print(str(num1) + " // " + str(num2) + " = " + str(result))

# To get more clarity in the answers printed I have chosen to print the
# answers showing the calculations. For this to be possible I have to
# use the str function on the variables to be able to mix them with strings .
