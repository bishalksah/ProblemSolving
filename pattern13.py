# 0101
# 1010
# 0101
# 1010 

for i in range(4):
    for j in range(4):
        if (i + j) % 2 == 0:
            print("0", end="")
        else:   
            print(1 , end = "")
    print()