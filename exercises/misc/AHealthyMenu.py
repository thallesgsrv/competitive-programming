N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]

resposta = 0
for j in range(M):
    maximo = max(G[i][j] for i in range(N))
    resposta += maximo

print(resposta)