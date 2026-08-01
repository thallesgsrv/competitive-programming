def BitwiseAND(n):
    if n <= 1:
        return 0
    res = 1
    while (res * 2) - 1 < n:
        res *= 2
    return res - 1
def main():
    for _ in range(int(input())):
        n = int(input())
        print(BitwiseAND(n))
main()

# This code is solving a problem where we need to find the largest integer `m` such that `m < n` and `m` is of the form `2^k - 1` for some non-negative integer `k`. The function `BitwiseAND(n)` calculates this value by starting with `res = 1` (which corresponds to `2^0 - 1`) and repeatedly doubling `res` until `res * 2 - 1` is no longer less than `n`. Once the loop ends, it returns `res - 1`, which is the largest integer of the form `2^k - 1` that is less than `n`. The main function reads multiple test cases, calls the `BitwiseAND` function for each input, and prints the result.
# The logic behind this is that numbers of the form `2^k - 1` have a binary representation consisting of `k` bits all set to 1. For example, `1` (which is `2^1 - 1`), `3` (which is `2^2 - 1`), `7` (which is `2^3 - 1`), and so on. The code efficiently finds the largest such number that is less than the given input `n`.