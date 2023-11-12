numbers = [5, 2, 3, 2, 4, 1]

sum_of_numbers = 0
for number in numbers:
    if number <= 2:
        sum_of_numbers += number
    else:
        sum_of_numbers += 1

print(sum_of_numbers)  # prints 8