n = int(input())
destinations = [0] + list(map(int, input().split()))
ans = [0] * (n + 1)
ans[n] = n

for i in range(n-1, 0, -1):
    if destinations[i] == i:
        ans[i] = i
    else:
        ans[i] = ans[destinations[i]]

print(*ans[1:])

    
    