for _ in range(int(input())):
    x = list(map(int, input().split()))
    print(2 * max(x) - sum(x))

# This code is solving a problem where we have three integers, and we need to determine the minimum number of moves required to make all three integers equal. The move consists of incrementing two of the integers by 1. The code calculates the maximum of the three integers and then uses the formula `2 * max(x) - sum(x)` to find the minimum number of moves needed to equalize all three integers.
# The logic behind the formula is that in each move, we can increase two integers, which effectively increases the total sum of the integers by 2. To make all integers equal to the maximum integer, we need to increase the sum of the integers to `3 * max(x)`. The difference between `3 * max(x)` and the current sum of the integers gives us the total increments needed, and since each move increments the sum by 2, we divide that difference by 2 to get the number of moves.
