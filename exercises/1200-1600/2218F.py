def main():

    for _ in range(int(input())):
        x, y = map(int, input().split())
        n = x + y
        d = y - x

        if (x == 0 and n % 2 == 0) or n//2<x:
            print("NO")
            continue

        print("YES")

        mm = 2 * x + (d % 2)

        for i in range(2, mm + 1):
            print(i-1, i)

        for i in range(mm+1, n+1):
            print(mm, i)


main()

# This code is solving a problem where we have two integers `x` and `y`, and we need to determine if it's possible to create a sequence of pairs of integers from 1 to `n` (where `n` is the sum of `x` and `y`) such that the number of pairs that can be formed with the first integer being less than or equal to `x` is equal to `x`, and the number of pairs that can be formed with the first integer being greater than `x` is equal to `y`.
# The code first checks if it's possible to create such pairs based on the values of `x` and `y`. If `x` is 0 and `n` is even, or if `n//2` is less than `x`, it prints "NO" and continues to the next test case. Otherwise, it prints "YES" and proceeds to generate the pairs.
# The variable `mm` is calculated as `2 * x + (d % 2)`, which determines the maximum integer that can be used in the pairs. The code then generates pairs from 1 to `mm` and from `mm+1` to `n`, ensuring that the pairs are formed according to the rules specified by `x` and `y`. Finally, it prints the pairs for each test case.       
