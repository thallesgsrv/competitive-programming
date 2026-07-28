n, d = map(int, input().split())
amigos = []

for _ in range(n):
    m, s = map(int, input().split())
    amigos.append((m, s))

amigos.sort()

soma = 0
resposta = 0
l = 0

for r in range(n):
    soma += amigos[r][1]
    
    while amigos[r][0] - amigos[l][0] >= d:
        soma -= amigos[l][1]
        l += 1
    
    resposta = max(resposta, soma)

print(resposta)