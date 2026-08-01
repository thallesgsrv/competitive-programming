from collections import deque

visitados = set()
def bfs(salas,no,visitados):
    fila = deque([no])
    visitados.add(no)

    while fila:
        no = fila.popleft()
        for caminho in salas[no]:
            if caminho not in visitados:
                visitados.add(caminho)
                fila.append(caminho)
    if len(visitados)== n:
        return "YES"
    else:
        return "NO"

n = int(input())
salas = []
for _ in range(n):
    dados = list(map(int,input().split()))
    k = dados[0]
    chv = dados[1:]
    salas.append(chv)

print(bfs(salas,0,visitados))
    