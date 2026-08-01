n = int(input())
b = list(map(int, input().split()))
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = b[i-1]

employee_count = [0] * (n+1)

ceos = []
for i in range(1, n+1):
    if parent[i] == 0:
        ceos.append(i)

for ceo in ceos:
    count = 0

    for i in range(1, n+1):
        if i == ceo:
            continue
        curr = i
    
        while curr != 0:
            if curr == ceo:
                count += 1
                break
            curr = parent[curr]
    employee_count[ceo] = count

max_ceo = ceos[0]
max_count = employee_count[ceos[0]]

for ceo in ceos:
    if employee_count[ceo] > max_count:
        max_count = employee_count[ceo]
        max_ceo = ceo

print(max_ceo, max_count+1)