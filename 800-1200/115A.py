def solve():
    n = int(input())
    parent = [0] * (n + 1)
    
    for i in range(1, n + 1):
        parent[i] = int(input())
    
    dp = [-1] * (n + 1)
    
    for i in range(1, n + 1):
        if dp[i] != -1:
            continue
        
        path = []
        curr = i
        
        while curr != -1 and dp[curr] == -1:
            path.append(curr)
            curr = parent[curr]
        
        if curr == -1:
            val = 0
        else:
            val = dp[curr]
        
        for node in reversed(path):
            val += 1
            dp[node] = val
    
    print(max(dp[1:]))

if __name__ == "__main__":
    solve()