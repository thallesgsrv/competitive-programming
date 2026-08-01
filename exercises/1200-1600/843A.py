def find(x, pais):
    if pais[x] < 0:
        return x
    pais[x] = find(pais[x], pais)
    return pais[x]

def union(a, b, pais):
    raiz_a = find(a, pais)
    raiz_b = find(b, pais)
    if raiz_a == raiz_b:
        return False
    
    if pais[raiz_b] < pais[raiz_a]:
        raiz_a, raiz_b = raiz_b, raiz_a
    pais[raiz_a] += pais[raiz_b]
    pais[raiz_b] = raiz_a
    return True

k = int(input())
ks = list(map(int, input().split()))
pais = [-1] * (k+1)

b = sorted(ks)
pos = {}
for i, x in enumerate(b, start=1):
    pos[x] = i
    
p = [0]

for x in ks:
    p.append(pos[x])

for i in range(1, k+1):
    union(i, p[i], pais)

grupos = {}
for i in range(1, k+1):
    raiz = find(i, pais)
    
    if raiz not in grupos:
        grupos[raiz] = []
        
    grupos[raiz].append(i) 
      
print(len(grupos))

for sub in grupos.values():
    print(len(sub), *sub)