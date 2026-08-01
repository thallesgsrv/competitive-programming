n = int(input())
Na = list(map(int, input().split()))
m = int(input())
Ma = list(map(int, input().split())) 

limites = [0] * n 
for i in range(n):
    limites[i] = Na[i] + limites[i-1] if i > 0 else Na[i]

for q in Ma:
    low, high = 0, n-1
    while low < high:
        mid = (low + high) // 2
        if q <= limites[mid]:
            high = mid
        else:
            low = mid + 1
    print(low + 1)

# This code is solving a problem where we have two lists of integers, `Na` and `Ma`. The list `Na` represents the number of items in different categories, and the list `Ma` contains queries that ask for the category index corresponding to a certain cumulative count. The code first calculates the cumulative sums of the `Na` list and stores them in the `limites` list. Then, for each query in `Ma`, it performs a binary search on the `limites` list to find the smallest index where the cumulative count is greater than or equal to the query value. Finally, it prints the category index (1-based) for each query.
# The binary search is efficient for this problem because the `limites` list is sorted in non-decreasing order, allowing us to quickly find the correct category index for each query.