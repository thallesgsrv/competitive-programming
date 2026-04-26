for _ in range(int(input())):
    x = list(map(int, input().split()))
    print(2 * max(x) - sum(x))