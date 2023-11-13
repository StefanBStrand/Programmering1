a = 5
b = 2
c = 0

c += a ** b
print(c)  # prints 25

c += a % b
print(c)  # prints 26

c += a - b * 2
print(c)  # prints 27

c //= b  # // floor division, rounds down to nearest whole number
print(c)  # prints 13

# Remember : PEMDAS rule for arithmetic:
# P for Parentheses, these evaluate first
# E for Exponents evaluate (raising to the power of)
# MD for Multiplication and Division, from left to right. They have the same precedence, so if they both appear in an
# expression, you evaluate them in the order they appear, moving from LEFt to RIGHT
# AS for Addition and Subtraction - these also from left to right in the order they appear!