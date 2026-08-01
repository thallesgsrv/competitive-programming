n, x = map(int, input().split())
a = list(map(int, input().split()))
dict = {}
lista = []

for i in range(n):
    target = x - a[i]
    if target in dict:
        lista.append(dict[target] + 1)
        lista.append(i + 1)
        break
    else:
        dict[a[i]] = i

if len(lista) == 0:
    print("IMPOSSIBLE")
else:
    print(" ".join(map(str, lista)))