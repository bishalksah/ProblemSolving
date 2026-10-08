#  Zigzag Pattern of Stars 
# Stars printed in a zigzag/wave form:
# plain
# *   *   *
#  * * * *
#   *   *

pattern = [
    "*   *   *",
    " * * * *",
    "  *   *"
]

for i in range(3):
    for j in range(len(pattern[i])):
        print(pattern[i][j], end="")
    print()