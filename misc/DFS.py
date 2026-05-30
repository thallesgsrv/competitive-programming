visitados = set()
def dfs(salas,no,visitados):
    if no is not None:
        visitados.add(no)
    for i in range(len(salas[no])):
        if salas[no][i] not in visitados:
            dfs(salas,salas[no][i],visitados)
    if len(visitados) == n:
        return "YES"
    else:
        return "NO"

n = int(input())
salas = []
for _ in range(n):
    dados = list(map(int,input().split()))
    quant_chaves = dados[0]
    chaves_portas = dados[1:]
    salas.append(chaves_portas)

print(dfs(salas, 0, visitados))
