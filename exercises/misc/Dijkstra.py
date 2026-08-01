from heapq import heappush, heappop
def dijkstra(grafo, inicio):
    n = len(grafo)
    dist = [float('inf')] * n
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

grafo = [ 
[(1, 4), (2, 1)],
[(3, 1)],
[(1, 2), (3, 5)],
[]
]


print(dijkstra(grafo, 0))