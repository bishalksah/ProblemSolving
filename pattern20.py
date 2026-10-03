# CCC
#  BB
#   A
 
n =0 
for i in range(3 ,0,-1):
    print(" "* n, end ="")
    n +=1
    for j in range(i):
        print(chr(64 + i) , end = "")
    print()