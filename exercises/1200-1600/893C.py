def dfs(u, visitados, adj, o, comp):
    visitados[u] = True
    comp.append(u)
    for v in adj[u]:
        if not visitados[v]:
            dfs(v, visitados, adj, o, comp)

n, m = map(int, input().split())
o = [0] + list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]

visitados = [False] * (n + 1)
total = 0 

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, n + 1):
    if not visitados[i]:
        comp = []
        dfs(i, visitados, adj, o, comp)
        total += min(o[j] for j in comp)

print(total)