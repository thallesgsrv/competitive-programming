n, m = map(int, input().split())
a = list(map(int, input().split()))

max_rodadas =0
ultimo = 0
for i in range(n):
    rodadas = (a[i] + m - 1) // m
    if rodadas >= max_rodadas:
        max_rodadas = rodadas
        ultimo = i + 1 
print(ultimo)
