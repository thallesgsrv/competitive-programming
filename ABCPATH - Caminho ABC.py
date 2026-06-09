import sys
sys.setrecursionlimit(10**6)

movimentos = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]

def dfs(i, j, h, w, grid, dp):
    if dp[i][j] != -1:
        return dp[i][j]
        
    melhor = 1
        
    for di, dj in movimentos:
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w:
            if ord(grid[ni][nj]) == ord(grid[i][j]) + 1:
                melhor = max(melhor, 1 + dfs(ni, nj, h, w, grid, dp))
        
    dp[i][j] = melhor
    return melhor

caso = 1  

while True:
    linha = sys.stdin.readline().strip()
    while linha == '':
        linha = sys.stdin.readline().strip()
        
    h, w = map(int, linha.split())
    if h == 0 and w == 0:
        break
        
    grid = []
    for _ in range(h):
        linha_grid = sys.stdin.readline().strip()
        grid.append(linha_grid)
        
    dp = [[-1] * w for _ in range(h)]
    
    maior_caminho = 0        
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'A':
                maior_caminho = max(maior_caminho, dfs(i, j, h, w, grid, dp))
        
    print(f"Case {caso}: {maior_caminho}")
    caso += 1