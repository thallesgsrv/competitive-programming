"""
DIJKSTRA (MENOR CAMINHO)
"""

from heapq import heappush, heappop

def dijkstra(grafo, inicio):
    """
    grafo: lista de adjacência [(vizinho, peso), ...]
    retorna: distâncias do início para todos os nós
    """
    n = len(grafo)
    dist = [float('inf')] * n
    dist[inicio] = 0
    heap = [(0, inicio)]

    while heap:
        dist_atual, no = heappop(heap)

        if dist_atual > dist[no]:
            continue

        for vizinho, peso in grafo[no]:
            nova_dist = dist[no] + peso
            if nova_dist < dist[vizinho]:
                dist[vizinho] = nova_dist
                heappush(heap, (nova_dist, vizinho))

    return dist

# ===== EXEMPLO DE USO =====
n, m = map(int, input().split())
grafo = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    grafo[u].append((v, w))

dist = dijkstra(grafo, 1)
print(*dist[1:])

# ===== NETWORK DELAY TIME (LEETCODE 743) =====
def network_delay_time(times, n, k):
    grafo = [[] for _ in range(n + 1)]
    for u, v, w in times:
        grafo[u].append((v, w))

    dist = dijkstra(grafo, k)

    max_dist = 0
    for i in range(1, n + 1):
        if dist[i] == float('inf'):
            return -1
        max_dist = max(max_dist, dist[i])

    return max_dist
