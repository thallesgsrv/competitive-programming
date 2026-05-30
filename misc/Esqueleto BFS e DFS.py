from collections import deque

def bfs(inicio, grafo, visitados):
    fila = deque([inicio])
    visitados.add(inicio)
    
    while fila:
        no = fila.popleft()
        print(no)
        
        for vizinho in grafo[no]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)


def dfs(no, grafo, visitados):
    visitados.add(no)
    print(no)
    
    for vizinho in grafo[no]:
        if vizinho not in visitados:
            dfs(vizinho, grafo, visitados)

grafo = {0: [1,2], 1: [0,3], 2: [0], 3: [1]}
visitados = set()
dfs(0, grafo, visitados)