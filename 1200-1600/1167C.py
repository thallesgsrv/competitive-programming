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
pais = [-1] * (n+1)

for i in range(m):
    dados = list(map(int, input().split()))
    k = dados[0]

    if k > 0:
        usuarios = dados[1:]
        primeiro = usuarios[0]

        for user in usuarios[1:]:
            union(primeiro, user, pais)

resultado = []

for i in range(1, n+1):
    raiz = find(i, pais)
    tamanho = -pais[raiz]
    resultado.append(tamanho)


print(" ".join(map(str, resultado)))