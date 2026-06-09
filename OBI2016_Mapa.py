import sys
sys.setrecursionlimit(100000)

visitados = set()

def dfs(mapa, inicio, visitados, ordem):
    visitados.add(inicio)
    ordem.append(inicio)
    movimento = [(-1,0),(0,-1),(1,0),(0,1)]
    
    for x, y in movimento:
        a, b = inicio[0] + x, inicio[1] + y
        if 0 <= a < len(mapa) and 0 <= b < len(mapa[0]):
            if mapa[a][b] == "H" or mapa[a][b] == "o":
                vizinho = (a, b)
                if vizinho not in visitados:
                    dfs(mapa, vizinho, visitados, ordem)

l, c = map(int, input().split())
mapa = [input() for _ in range(l)]
inicio = None
ordem = []

for i in range(l):
    for j in range(c):
        if mapa[i][j] == "o":
            inicio = (i, j)
            break
    if inicio:
        break

if inicio:
    dfs(mapa, inicio, visitados, ordem)
    if ordem:
        resultado = (ordem[-1][0] + 1, ordem[-1][1] + 1)
        print(*resultado)