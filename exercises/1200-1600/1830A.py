from collections import deque

def bfs(grafo, inicio, pos):
    fila = deque()
    leituras_vertice = {}
    leituras_vertice[inicio] = 1
    
    for v in grafo[inicio]:
        fila.append((v, inicio, 1, pos[(inicio, v)]))
    
    resposta = 1
    
    while fila:
        no, pai, leit, pos_pai = fila.popleft()
        
        resposta = max(resposta, leit)
        leituras_vertice[no] = leit
        
        for vizinho in grafo[no]:
            if vizinho == pai:
                continue
            
            pos_atual = pos[(no, vizinho)]
            
            if pos_atual < pos_pai:
                fila.append((vizinho, no, leit + 1, pos_atual))
            else:
                fila.append((vizinho, no, leit, pos_atual))
    
    return resposta


t = int(input())
for _ in range(t):
    n = int(input())
    adj = [[] for _ in range(n + 1)]
    pos = {}
    
    for i in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        pos[(u, v)] = i
        pos[(v, u)] = i
    
    leituras = bfs(adj, 1, pos)
    print(leituras)