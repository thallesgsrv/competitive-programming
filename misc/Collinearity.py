def colineares(a,b,c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return (x2 - x1)*(y3 - y1) == (y2 - y1)*(x3 - x1)

pontos = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    pontos.append((x,y))

encontrou = False
for i in range(len(pontos)):
    for j in range(i+1, len(pontos)):
        for t in range(j+1, len(pontos)):
            if colineares(pontos[i], pontos[j], pontos[t]):
                encontrou = True
                break
        if encontrou:
            break
    if encontrou:
        break

if encontrou:
    print("Yes")
else: 
    print("No")