n = int(input())
a = list(map(int, input().split()))
freq = {}

for valor in a:
    freq[valor] = freq.get(valor, 0) + 1

total_pares = sum(quantidade // 2 for quantidade in freq.values())
print(total_pares)