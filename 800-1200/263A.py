matriz = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        if matriz[i][j] == 1:
            linha = i + 1
            coluna = j + 1

movimentos = abs(linha - 3) + abs(coluna - 3)

print(movimentos)