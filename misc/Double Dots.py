from collections import deque

N, M = map(int, input().split())

grafo = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    grafo[a].append(b)
    grafo[b].append(a)

dist = [-1] * (N + 1)
dist[1] = 0
fila = deque([1])

while fila:
    atual = fila.popleft()
    for vizinho in grafo[atual]:
        if dist[vizinho] == -1:
            dist[vizinho] = dist[atual] + 1
            fila.append(vizinho)

placa = [0] * (N + 1)

for sala in range(2, N + 1):
    encontrou = False
    for vizinho in grafo[sala]:
        if dist[vizinho] == dist[sala] - 1:
            placa[sala] = vizinho
            encontrou = True
            break
    
    if not encontrou:
        print("No")
        exit() 

print("Yes")
for sala in range(2, N + 1):
    print(placa[sala])