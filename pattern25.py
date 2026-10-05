# Character Pyramid (Problems: 27, 45)
# Print characters forming a pyramid (character changes each row):

#     A
#    B B
#   C C C
#  D D D D
# E E E E E


n = 5

for i in range(n):
    for j in range(n - i -1):
        print("", end=" ")

    for j in range(i + 1):
        print(chr(65 + i), end=" ")

    print()