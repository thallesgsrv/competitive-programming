from heapq import heappush, heappop
def dijkstra(n,grafo,inicio):
    dist = [float('inf')] * (n+1)
    dist[inicio] = 0

    heap = [(0, inicio)]

    while heap:
        distancia_atual, no = heappop(heap)
        
        if distancia_atual > dist[no]:
            continue

        for vizinho, peso in grafo[no]:
            nova_dist = dist[no] + peso
            if nova_dist < dist[vizinho]:
                dist[vizinho] = nova_dist

                heappush(heap, (nova_dist, vizinho))
    
    return dist

n, m = map(int, input().split())
grafo = [[]for i in range(n+1)]
menor_p = float('inf')
for _ in range(m):
    u, v, p = map(int, input().split())
    if p < menor_p:
        menor_p = p
    grafo[u].append((v,p))
    grafo[v].append((u,p))

inicio = int(input())
distancias = dijkstra(n,grafo,inicio)

distancias_sem_o_inicio = []
for i in range(1, n+1):
    if i != inicio:
        distancias_sem_o_inicio.append(distancias[i])

resultado = max(distancias_sem_o_inicio) - min(distancias_sem_o_inicio)

print(resultado)