# Diagonal Lines (Problem: 28)
# Print numbers only on the diagonals of a square, spaces elsewhere:

# 1     3
#   2 2
# 1  2  1
#   2 2
# 3     1

n = 5
for i in range(n):
    for j in range(n):
        if (i == 0 and j in [0, 4]):
            print(1 if j == 0 else 3, end="")
        elif (i == 4 and j in [0, 4]):
            print(3 if j == 0 else 1, end="")
        elif (i in [1, 3] and j in [1, 3]):
            print(2, end="")
        elif (i == 2 and j in [0, 2, 4]):
            print(2 if j == 2 else 1, end="")
        else:
            print(" ", end="")
    print()
    
     