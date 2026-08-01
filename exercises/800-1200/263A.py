matriz = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        if matriz[i][j] == 1:
            linha = i + 1
            coluna = j + 1

movimentos = abs(linha - 3) + abs(coluna - 3)

print(movimentos)

# This code is solving a problem where we have a 5x5 matrix, and we need to find the position of the element with the value `1`. Once we find the position of `1`, we calculate the number of moves required to bring it to the center of the matrix (which is at position (3, 3) in 1-based indexing). The number of moves is calculated as the sum of the absolute differences between the current row and column of `1` and the target row and column (which are both 3). Finally, it prints the total number of moves required.
# The logic behind this is that we are essentially calculating the Manhattan distance from the current position of `1` to the center of the matrix. The Manhattan distance is given by the formula `abs(x1 - x2) + abs(y1 - y2)`, where `(x1, y1)` is the current position and `(x2, y2)` is the target position. In this case, the target position is (3, 3), so we use that in our calculation. The code iterates through the matrix to find the position of `1`, and once found, it computes and prints the required moves.
# For example, if the input matrix is:
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 1 0 0 
# 0 0 0 0 0
# 0 0 0 0 0
# The position of `1` is at (3, 3), which is already the center, so the number of moves required is `0`. If the input matrix is:
# 0 0 0 0 0
# 0 0 0 0 0
# 0 1 0 0 0
# 0 0 0 0 0 
# 0 0 0 0 0
# The position of `1` is at (3, 2), so the number of moves required to bring it to (3, 3) is `abs(3 - 3) + abs(2 - 3) = 1`. Therefore, the output will be `1`.
# The code efficiently finds the position of `1` and calculates the required moves in a straightforward manner, making it easy to understand and implement. 