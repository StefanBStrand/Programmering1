x = 0

for i in range(0, 5, 2):
    x += i

print(x)

# 1: i = 0 and x = 0
# 2: i = 2 and x becomes 2 from adding i
# 3: i = 4 and x becomes 6 from adding i (when it was 2 in the last iteration)

y = 0

for j in range(0, 5):
    y += j

print(y)

# 1: j = 0 and y = 0
# 2: j =