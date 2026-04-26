for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    tot = sum(arr)
    
    if tot % 2 == 1 or (n * k) % 2 == 0:
        print("YES")
    else:
        print("NO")