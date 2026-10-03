# 18. Spiral Matrix (Problem: 21)
# Fill a square matrix in spiral order starting from the top-left, moving right → down → left → up:
# plain
# Input: 3
# 1 2 3
# 8 9 4
# 7 6 5


n = 3

matrix = [[0] * n for _ in range(n)]

top = 0
bottom = n - 1
left = 0
right = n - 1

num = 1

while top <= bottom and left <= right:
    for j in range(left , right +1):
        matrix[top][j] = num
        num += 1
    top += 1 
    
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    # Left
    for j in range(right, left - 1, -1):
        matrix[bottom][j] = num
        num += 1
    bottom -= 1

    # Up
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1
        
for row in matrix:
    print(*row)    
    