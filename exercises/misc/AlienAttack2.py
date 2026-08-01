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

def tamanho(x):
    pai = find(x, pais)
    return -pais[pai]

n, m = map(int, input().split())
pais = [-1] * (n+1)
minimo = 0
if m == 0:
    minimo = 1

for _ in range(m):
    a, b = map(int, input().split())
    union(a,b, pais)
    if tamanho(a) > minimo:
        minimo = tamanho(a)

print(minimo)