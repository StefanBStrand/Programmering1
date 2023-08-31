a = 6
b = 3
c = 2

result = a + b * c
print(str(a) + " + " + str(b) + " * " + str(c) + " = " + str(result))

result = (a + b) * c
print("(" + str(a) + " + " + str(b) + ")" + " * " + str(c) + " = " + str(result))

result = a / b / c
print(str(a) + " / " + str(b) + " / " + str(c) + " = " + str(result))

result = a / (b / c)
print(str(a) + " / " + "(" + str(b) + " / " + str(c) + ")" + " = " + str(result))