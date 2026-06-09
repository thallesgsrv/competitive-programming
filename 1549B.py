def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        enemy = input().strip()
        gregor = input().strip()
        
        used = [False] * n
        ans = 0
        
        for i in range(n):
            if gregor[i] == '1':
                if enemy[i] == '0':
                    ans += 1
                else:
                    if i > 0 and enemy[i-1] == '1' and not used[i-1]:
                        ans += 1
                        used[i-1] = True
                    elif i < n-1 and enemy[i+1] == '1' and not used[i+1]:
                        ans += 1
                        used[i+1] = True
        
        print(ans)

if __name__ == "__main__":
    solve()