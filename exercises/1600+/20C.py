from heapq import heappush, heappop
def dijkstra(grafo,n, inicio, fim):
    dist = [float('inf')] * (n + 1)
    dist[inicio] = 0
    pai = [-1] * (n+1)

    heap = [(0, inicio)]

    while heap:

        distancia_atual, no = heappop(heap)

        if distancia_atual > dist[no]:
            continue
        if no == fim:
            break 
        for vizinho, peso in grafo[no]:
            nova_dist = dist[no] + peso
            if nova_dist < dist[vizinho]:
                dist[vizinho]= nova_dist 
                pai[vizinho] = no
                heappush(heap, (nova_dist, vizinho))
    
    if dist[fim] == float('inf'):
        return -1, []

    caminho = []
    atual = fim
    while atual != -1:
        caminho.append(atual)
        atual = pai[atual]

    caminho.reverse()
    return dist[fim], caminho        

n, m = map(int, input().split())
grafo = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    grafo[a].append((b, c))
    grafo[b].append((a, c))

distancia, caminho = dijkstra(grafo, n, 1, n)

if distancia == -1:
    print(-1)
else:
    print(' '.join(map(str, caminho)))