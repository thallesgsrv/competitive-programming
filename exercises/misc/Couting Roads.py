n, m = map(int, input().split())

graus = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graus[a] += 1
    graus[b] += 1
for i in range(1, n + 1):
    print(graus[i])