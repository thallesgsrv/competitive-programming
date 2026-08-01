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

# This code is solving a problem where we have `n` machines, each with a certain production time given in the list `k`. We want to find the minimum time required to produce at least `t` items.
# The function `total_produzido(T, k)` calculates how many items can be produced in time `T` by summing up the number of items each machine can produce, which is given by `T // tempo` for each machine's production time `tempo`. If the total produced items is greater than or equal to `t`, it returns `t` to avoid unnecessary calculations.
# The main part of the code uses a binary search to find the minimum time `low` such that `total_produzido(low, k)` is at least `t`. It initializes `low` to 1 and `high` to a very large number (10^18) to ensure it covers all possible times. The binary search continues until `low` is less than `high`, and it updates `low` and `high` based on whether the total produced items at time `mid` meets the requirement of at least `t` items. Finally, it prints the minimum time found.
