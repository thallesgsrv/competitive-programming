arrInitial = [1, 2, 3]
total = 2**len(arrInitial)
Subsets = []
for mask in range(0, total):
    subset = []
    for i in range(len(arrInitial)):
        if mask & (1 << i) != 0:
            subset.append(arrInitial[i])
    Subsets.append(subset)
print(Subsets)

# This code generates all possible subsets of the given list `arrInitial` using bit manipulation. The total number of subsets is calculated as `2` raised to the power of the length of the input list, which accounts for every combination of including or excluding each element. The outer loop iterates through all possible combinations (from `0` to `total - 1`), and the inner loop checks which elements are included in the current subset based on the bits set in the `mask`. If a bit is set, the corresponding element from `arrInitial` is added to the current subset. Finally, all subsets are collected in the `Subsets` list and printed.
