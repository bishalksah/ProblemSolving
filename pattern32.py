#  Cross Pattern of Numbers (Problem: 47)
# Numbers arranged in a plus (+) shape:
# plain
#   1
#   2
# 34567
#   6
#   5


n = 5
num = 1
for i in range(n):
    for j in range(n):
        if i == 2:
            print(j+3, end ="")
            
        elif j == 2:
            if i < 2:
                print(i + 1, end="")
            else:
                print(9 - i, end="")
        else:
            print(" ", end="")
    print()