"""
KRUSKAL - ÁRVORE GERADORA MÍNIMA (MST)
"""

def kruskal(n, arestas):
    """
    n: número de vértices
    arestas: [(peso, u, v), ...]
    retorna: (custo_total, arvore) ou None
    """
    arestas.sort()
    dsu = DSU(n)
    custo_total = 0
    arvore = []
    arestas_usadas = 0

    for peso, u, v in arestas:
        if dsu.union(u, v):
            custo_total += peso
            arvore.append((u, v, peso))
            arestas_usadas += 1

            if arestas_usadas == n - 1:
                break

    if arestas_usadas != n - 1:
        return None

    return custo_total, arvore

# ===== EXEMPLO DE USO =====
n, m = map(int, input().split())
arestas = []

for _ in range(m):
    u, v, peso = map(int, input().split())
    arestas.append((peso, u, v))

resultado = kruskal(n, arestas)
if resultado is None:
    print(-1)
else:
    custo, _ = resultado
    print(custo)
