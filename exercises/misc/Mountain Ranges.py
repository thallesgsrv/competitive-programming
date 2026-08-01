n, m = map(int, input().split())
h = list(map(int, input().split()))

low, high = 1, 1000000
k = -1
while low <= high:
    mid = (low + high)// 2
    total = 1
    for i in range(n-1):
        if abs(h[i]-h[i+1]) > mid:
            total+=1 
    
    if total <= m:
        k = mid
        high = mid - 1
    else:
        low = mid + 1
total1= 1
for i in range(n-1):
    if abs(h[i]-h[i+1]) > k:
        total1+=1

if total1 == m:
    print(k)
else:
    print(-1)

    

