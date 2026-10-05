#   1
#  232
# 34543

n = 3
for i in range(1 ,n+1):
    print(" " *(n - i) , end ="")
    for j in range(i , 2 * i):
        print(j , end ="")
    for j in range(2*i - 2, i - 1, -1):
        print(j, end ="")
    print()
    
        
    
    