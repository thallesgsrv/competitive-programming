visitados = set()
def dfs(grafo, no, visitados):
    if no not in visitados:
        visitados.add(no)
        for vizinho in grafo[no] :
            if vizinho not in visitados:
                dfs(grafo,vizinho,visitados)

n, m = map(int,input().split())
grafo = [[]for _ in range(n+1)]
for _ in range(m):
    dados = list(map(int, input().split()))
    no = dados[0]
    n2 = dados[1]
    grafo[no].append(n2)    
    grafo[n2].append(no)
    
componente = 0
for v in range(1,n+1):
    if v not in visitados:
        componente +=1
        (dfs(grafo,v,visitados))
print(componente)
