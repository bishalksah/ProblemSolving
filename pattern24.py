# 20. Alternating Characters Matrix (Problems: 26, 42)
# Fill the matrix with alternating characters (e.g., * and #, or A and B):


# * # * #
# # * # *
# * # * #
# # * # *

n = 4

for i in range(n):
    for j in range(n+1):
        if (i + j) % 2 == 0:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()