"""
UNION-FIND (DSU) - DISJOINT SET UNION
"""

class DSU:
    def __init__(self, n):
        self.pai = [-1] * (n + 1)
        self.componentes = n

    def find(self, x):
        if self.pai[x] < 0:
            return x
        self.pai[x] = self.find(self.pai[x])
        return self.pai[x]

    def union(self, a, b):
        raiz_a = self.find(a)
        raiz_b = self.find(b)

        if raiz_a == raiz_b:
            return False

        if self.pai[raiz_b] < self.pai[raiz_a]:
            raiz_a, raiz_b = raiz_b, raiz_a

        self.pai[raiz_a] += self.pai[raiz_b]
        self.pai[raiz_b] = raiz_a
        self.componentes -= 1
        return True

    def tamanho(self, x):
        return -self.pai[self.find(x)]

    def mesmo_conjunto(self, a, b):
        return self.find(a) == self.find(b)

# ===== EXEMPLO DE USO =====
n, m = map(int, input().split())
dsu = DSU(n)

for _ in range(m):
    u, v = map(int, input().split())
    dsu.union(u, v)

print(dsu.componentes)

# ===== ARESTA REDUNDANTE (LEETCODE 684) =====
def find_redundant_connection(edges):
    n = len(edges)
    dsu = DSU(n)

    for u, v in edges:
        if not dsu.union(u, v):
            return [u, v]
    return []
