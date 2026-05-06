n, x = map(int, input().split())
a = list(map(int, input().split()))

arr = [(a[i], i + 1) for i in range(n)]
arr.sort()

left = 0
right = n - 1

while left < right:
    soma = arr[left][0] + arr[right][0]
    
    if soma == x:
        i1 = arr[left][1]
        i2 = arr[right][1]
        
        if i1 > i2:
            i1, i2 = i2, i1
        
        print(i1, i2)
        break
    elif soma < x:
        left += 1
    else:
        right -= 1
else:
    print("IMPOSSIBLE")