n = int(input())
if n != 0:
    if n & (n - 1) == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")

# This code is checking if a given integer `n` is a power of two. A number that is a power of two has exactly one bit set in its binary representation. The condition `n & (n - 1) == 0` checks if there is only one bit set in `n`. If `n` is not zero and satisfies this condition, it prints "YES"; otherwise, it prints "NO".