"""
GRAFOS (DFS/BFS)
"""

from collections import deque

# ===== DFS (LISTA DE ADJACÊNCIA) =====
def dfs(grafo, no, visitado):
    visitado.add(no)

    for vizinho in grafo[no]:
        if vizinho not in visitado:
            dfs(grafo, vizinho, visitado)

# ===== BFS (LISTA DE ADJACÊNCIA) =====
def bfs(grafo, inicio):
    visitado = {inicio}
    fila = deque([inicio])
    ordem = []

    while fila:
        no = fila.popleft()
        ordem.append(no)

        for vizinho in grafo[no]:
            if vizinho not in visitado:
                visitado.add(vizinho)
                fila.append(vizinho)

    return ordem

# ===== CONTAR COMPONENTES CONEXOS =====
def componentes_conexos(grafo):
    n = len(grafo)
    visitado = set()
    componentes = 0

    for no in range(n):
        if no not in visitado:
            componentes += 1
            dfs(grafo, no, visitado)

    return componentes

# ===== VERIFICAR CAMINHO ENTRE DOIS NÓS =====
def existe_caminho(grafo, source, dest):
    visitado = set()

    def dfs(no):
        if no == dest:
            return True
        visitado.add(no)
        for vizinho in grafo[no]:
            if vizinho not in visitado:
                if dfs(vizinho):
                    return True
        return False

    return dfs(source)

# ===== KEYS AND ROOMS (LEETCODE 841) =====
def pode_visitar_todas(rooms):
    visitado = set()

    def dfs(sala):
        visitado.add(sala)
        for chave in rooms[sala]:
            if chave not in visitado:
                dfs(chave)

    dfs(0)
    return len(visitado) == len(rooms)
