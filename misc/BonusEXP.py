n = int(input())
a = list(map(int, input().split()))

NEG = -10**18
dp = [0, NEG]

for x in a:
    ndp = dp[:]
    ndp[1] = max(ndp[1], dp[0] + x)
    ndp[0] = max(ndp[0], dp[1] + 2 * x)
    dp = ndp

print(max(dp))