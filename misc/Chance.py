maxm = 100000

primo = {2,3,5,7,11,13,17}
prefix = [0] *(maxm+1)

for num in range(maxm+1):
    uns = bin(num).count("1")
    if uns in primo:
        prefix[num] = 1
    else:
        prefix[num] = 0
    if num > 0:
        prefix[num] += prefix[num-1]

resultado = []
for _ in range(int(input())):
    l, r = map(int, input().split())
    if l == 0:
        resposta = prefix[r]
    else:
        resposta = prefix[r] - prefix[l-1]
    resultado.append(str(resposta))

print("\n".join(resultado))