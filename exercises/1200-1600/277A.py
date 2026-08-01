def find(x, pais):
    if pais[x] < 0:
        return x
    pais[x] = find(pais[x], pais)
    return pais[x]

def union(a,b,pais):
    raiz_a = find(a, pais)
    raiz_b = find(b, pais)
    if raiz_a == raiz_b:
        return False
    
    if pais[raiz_b] < pais[raiz_a]:
        raiz_a, raiz_b = raiz_b, raiz_a

    pais[raiz_a] += pais[raiz_b]
    pais[raiz_b] = raiz_a
    return True 

n, m = map(int, input().split())
pais = [-1] * (n+m)
grafo = [] 
tem_zero = True

for _ in range(n):
    dados = list(map(int, input().split()))
    k = dados[0]
    if k > 0:
        tem_zero = False
        grafo.append(dados[1:])
    else:
        grafo.append([])

if tem_zero:
    print(n)

else:
    for i in range(n):
        for lingua in grafo[i]:
            union(i, n + (lingua-1), pais)

    componentes = set()

    for i in range(n):
        componentes.add(find(i, pais))
    print(len(componentes)-1)