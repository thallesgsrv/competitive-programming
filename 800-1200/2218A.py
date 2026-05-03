for _ in range(int(input())):
    x = int(input())
    if x < 67:
        print(x+1)
    else:
        print(67)

# This code is solving a problem where we have an integer `x`, and we need to determine the next integer that is greater than `x` but does not exceed 67. If `x` is less than 67, it simply returns `x + 1`. If `x` is 67 or greater, it returns 67. This ensures that the output is always the smallest integer greater than `x` that does not exceed 67.
# The code reads multiple test cases, where each test case consists of a single integer `x`. For each test case, it applies the logic described above and prints the result.
