for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    tot = sum(arr)
    
    if tot % 2 == 1 or (n * k) % 2 == 0:
        print("YES")
    else:
        print("NO")

# This code is solving a problem where we have `n` integers and a parameter `k`, and we need to determine if it's possible to partition the integers into `k` subsets such that the sum of each subset is odd. The code first calculates the total sum of the integers. If the total sum is odd or if the product of `n` and `k` is even, it prints "YES", indicating that such a partition is possible. Otherwise, it prints "NO".
# The logic behind this is that for a partition to have all subsets with odd sums, the total sum must be odd (since the sum of odd numbers is odd), and the number of subsets must be odd (since the sum of an even number of odd numbers is even). Therefore, if
# the total sum is odd or if `n * k` is even, it means that we can achieve the required partitioning. If both conditions are not met, it means that it's not possible to partition the integers as required.
