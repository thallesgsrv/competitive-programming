for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    freq = [0] * (n+1)

    for x in a:
        freq[x] += 1
    
    for d in range(n, 0, -1):
        apagar = 0
        limite = min(2*d, n)

        for i in range(1, limite + 1):
            if i % d != 0:
                apagar+= freq[i]
        
        if apagar <= k:
            print(f"{d}a")
            break



