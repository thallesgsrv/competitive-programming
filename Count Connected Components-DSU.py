def find(x, pais):
    if pais[x] < 0:
        return x
    pais[x] = find(pais[x], pais)
    return pais[x]

def union(a,b,pais):
    raiz_a = find(a,pais)
    raiz_b = find(b,pais)
    if raiz_a == raiz_b:
        return False
    if pais[raiz_b] < pais[raiz_a]:
        pais[raiz_a], pais[raiz_b] = pais[raiz_b], pais[raiz_a]

    pais[raiz_a] += pais[raiz_b]
    pais[raiz_b] = raiz_a
    return True

N, M = map(int, input().split())

pais = [-1] * (N+1)

for _ in range(M):
    a, b = map(int,input().split())
    union(a,b, pais)

componnent = 0 

for elem in pais:
    if elem < 0:
        componnent+=1

print(componnent-1)