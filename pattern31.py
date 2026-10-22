# 25. Snake / Boustrophedon Matrix (Problem: 41)
# Same zigzag filling as #19 — fill the matrix in a continuous snake path:
# plain
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

    if i % 2 != 0:
        row.reverse()

    for x in row:
        print(x, end=" ")

    print()