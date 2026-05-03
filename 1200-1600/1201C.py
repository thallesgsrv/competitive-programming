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

# This code is solving a problem where we have `n` integers in a list `a`, and we want to find the maximum integer `low` such that we can increase some of the integers in the second half of the sorted list (from index `mid` to `n-1`) to at least `low` using at most `k` increments. The code uses a binary search approach to find this maximum integer. It calculates the total increments needed to raise the integers in the second half of the list to at least `target`, and adjusts the search range based on whether the total increments exceed `k`. Finally, it prints the maximum integer found. 
