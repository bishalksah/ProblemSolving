# 1 2 3 4
#   3 4
#     4

n = 4
for i in range(n-1):
    for s in range(i):
        print("  " ,end = "")
    
    start = 1 if i == 0 else i+2
    
    for j in range (start, n+1):
        print(j , end =" ")
        
    print()