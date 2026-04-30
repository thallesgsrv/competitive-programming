def total_produzido(T, k):
    soma = 0
    for tempo in k:
        soma += T // tempo
        if soma >= t:
            return t
    return soma

n, t = map(int, input().split())
k = list(map(int, input().split()))

low, high = 1, 10**18
while low < high:
    mid = (low + high) // 2
    if total_produzido(mid, k) >= t:
        high = mid
    else:
        low = mid + 1

print(low)