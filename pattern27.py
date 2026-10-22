# 1 2 3 4 5
#  2 3 4
#    3
#  2 3 4
# 1 2 3 4 5

n = 5

for i in range(n):
    if i <= 2:
        start = i + 1
        end = n - i
    else:
        start = n - i
        end = i + 1
        
    if (i == 2 ):
        print(" " * 3 , end="")
    elif (i in [1,3]):
        print (" "* 1, end = "")

    for j in range(start, end + 1):
        print(j, end=" ")

    print()