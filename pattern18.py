# XOXO
# OXOX
# XOXO
# OXOX

for i in range(4):
    for j in range(4):
        if (i+j) % 2 == 0:
            print("X" , end ="")
        else:
            print("O" ,end ="")
    print()
        