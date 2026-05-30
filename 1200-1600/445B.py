def find(x, pais):
    if pais[x] < 0:
        return x
    pais[x] = find(pais[x], pais)
    return pais[x]

def union(a,b,pais):
    raiz_a = find(a, pais)
    raiz_b = find(b, pais)
    if pais[raiz_a] == pais[raiz_b]:

        return False 
    
    if pais[raiz_b] < pais[raiz_a]:
        raiz_a, raiz_b = raiz_b, raiz_a

    pais[raiz_a] += pais[raiz_b]
    pais[raiz_b] = raiz_a
    return True

n, m = map(int,input().split())
pais = [-1] * (n+1)
raizes = set()

for _ in range(m):
    x, y = map(int, input().split())
    union(x,y,pais)

for i in range(1, n+1):
    raizes.add(find(i, pais))

c = len(raizes)

resultado = 1 << (n - c)

print(resultado)
