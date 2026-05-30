import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
mapa = [list(input().strip()) for _ in range(n)]

def bfs(i, j):
    fila = deque()
    fila.append((i, j))
    mapa[i][j] = '#'
    
    while fila:
        i, j = fila.popleft()
        
        if i + 1 < n and mapa[i+1][j] == '.':
            mapa[i+1][j] = '#'
            fila.append((i+1, j))
        if i - 1 >= 0 and mapa[i-1][j] == '.':
            mapa[i-1][j] = '#'
            fila.append((i-1, j))
        if j + 1 < m and mapa[i][j+1] == '.':
            mapa[i][j+1] = '#'
            fila.append((i, j+1))
        if j - 1 >= 0 and mapa[i][j-1] == '.':
            mapa[i][j-1] = '#'
            fila.append((i, j-1))

comodos = 0
for i in range(n):
    for j in range(m):
        if mapa[i][j] == '.':
            comodos += 1
            bfs(i, j)

print(comodos)