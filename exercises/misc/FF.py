n, q = map(int, input().split())

conjuntos = {}

for i in range(q):
    t, a, b = map(int, input().split())
    
    if t == 1:
        if a not in conjuntos:
            conjuntos[a] = set()
        conjuntos[a].add(b)
        
    elif t == 2:
        if a in conjuntos:
            conjuntos[a].discard(b)
            
    elif t == 3:
        if (a in conjuntos and b in conjuntos[a]) and \
           (b in conjuntos and a in conjuntos[b]):
            print("Yes")
        else:
            print("No")