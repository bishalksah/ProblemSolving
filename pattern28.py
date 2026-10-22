# 1       5
#   2   4
#     3
#   2   4
# 1       5



n = 5

for i in range(n):
    for j in range(n):
        
        if i == 0 or i == 4:
            if j == 0:
                print(1, end="")
            elif j == 4:
                print(5, end="")
            else:
                print(" ", end=" ")

        elif i == 1 or i == 3:
            if j == 1:
                print(2, end="")
            elif j == 3:
                print(4, end="")
            else:
                print(" ", end=" ")

        elif i == 2:
            if j == 2:
                print(3, end="")
            else:
                print(" ", end=" ")

    print()