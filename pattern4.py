# *****
#  ****
#   ***
#    **
#     *

for i in range(5):
    for j in range(i):
        print(" " , end ="")
    for j in range(5-i):   
        print("*" , end ="")
    print()
    
# shortest way to print this pattern  
for i in range(5):
    print(" " * i + "*" * (5-i))
    