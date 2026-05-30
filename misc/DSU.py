def kruskal(n, arestas):
    arestas.sort()
    pais = [-1] * (n+1)
    custo_total = 0
    arvore = []

    for peso,a,b in arestas:
        if union(a,b, pais):
            custo_total += peso
            arvore.append((peso,a,b))

            if len(arvore) == n-1:
                break
    if len(arvore) != n-1:
        return None

    return arvore, custo_total

def find(x, pais):
    if pais[x] < 0:
        return x
    pais[x] = find(pais[x], pais)
    return pais[x]


def union(a,b, pais):
    raiz_a = find(a, pais)
    raiz_b = find(b, pais)
    if raiz_a == raiz_b:
        return False
    
    if pais[raiz_b] < pais[raiz_a]:
        raiz_a, raiz_b = raiz_b, raiz_a
    
    pais[raiz_a] += pais[raiz_b]
    pais[raiz_b] = raiz_a
    return True

n = int(input())
pontos = []
arestas = []
for _ in range(n):
    a, b = map(int, input().split())
    pontos.append((a, b))
for i in range(n):
    x1, y1 = pontos[i]
    for j in range(i+1, n):
        x2, y2 = pontos[j]
        custo = abs(x1-x2)+ abs(y1-y2)
        arestas.append((custo, i, j))

resultado = kruskal(n, arestas)
if resultado is None:
    print(-1)
else:
    arvore, custo_total = resultado
    print(custo_total)