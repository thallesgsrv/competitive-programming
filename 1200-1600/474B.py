n = int(input())
Na = list(map(int, input().split()))
m = int(input())
Ma = list(map(int, input().split())) 

limites = [0] * n 
for i in range(n):
    limites[i] = Na[i] + limites[i-1] if i > 0 else Na[i]

for q in Ma:
    low, high = 0, n-1
    while low < high:
        mid = (low + high) // 2
        if q <= limites[mid]:
            high = mid
        else:
            low = mid + 1
    print(low + 1)