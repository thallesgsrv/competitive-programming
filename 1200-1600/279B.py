n, t = map(int, input().split())
Ni = list(map(int, input().split()))

j = 0
soma = 0
max_livros = 0

for i in range(n):
    if j < i:
        j = i
        soma = 0         
    while j < n and soma + Ni[j] <= t:
        soma += Ni[j]
        j += 1               
    
    max_livros = max(max_livros, j - i)
    soma -= Ni[i]
print(max_livros)