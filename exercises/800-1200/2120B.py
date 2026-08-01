t = int(input())
for _ in range(t):
    n, s = map(int,input().split())
    cont = 0
    for _ in range(n):
        dx, dy, x, y = map(int,input().split())
        if ((dx*y) - (dy*x)) % s == 0:
            cont+=1 
    print(cont)