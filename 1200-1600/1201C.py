n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

mid = n // 2
low, high = a[mid], a[mid] + k

while low < high:
    target = (low + high + 1) // 2
    total = 0
    for i in range(mid, n):
        if a[i] < target:
            total += target - a[i]
            if total > k:
                break
    
    if total <= k:
        low = target
    else:
        high = target - 1

print(low)