"""
ORDENAÇÃO TOPOLÓGICA (DAG)
"""

def ordenacao_topologica(grafo):
    n = len(grafo)
    visitado = set()
    processado = set()
    ordem = []

    def dfs(no):
        visitado.add(no)

        for vizinho in grafo[no]:
            if vizinho in visitado:
                return False
            if vizinho not in processado:
                if not dfs(vizinho):
                    return False

        visitado.remove(no)
        processado.add(no)
        ordem.append(no)
        return True

    for no in range(n):
        if no not in processado:
            if not dfs(no):
                return None

    ordem.reverse()
    return ordem

# ===== EXEMPLO DE USO (CSES 1679) =====
n, m = map(int, input().split())
grafo = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    grafo[a].append(b)

ordem = ordenacao_topologica(grafo)
if ordem is None:
    print("IMPOSSIBLE")
else:
    print(*[x + 1 for x in ordem])
