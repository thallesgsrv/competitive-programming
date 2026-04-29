n, m = map(int, input().split())

cidades = list(map(int, input().split()))
torres = list(map(int, input().split()))

j = 0 
max_distancia = 0
for c in cidades:
    while j + 1 < m and abs(c - torres[j]) >= abs(c - torres[j + 1]):
        j += 1
    
    distacia = abs(c - torres[j])
    max_distancia = max(max_distancia, distacia)

print(max_distancia)