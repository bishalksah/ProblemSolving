# 1 2 3
# 6 5 4
# 7 8 9

n = 3
num = 1

for i in range(n):
    row = []

    for j in range(n):
        row.append(num)
        num += 1

    if i % 2 == 1:
        row.reverse()

    print(*row)