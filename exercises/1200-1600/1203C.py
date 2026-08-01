from math import gcd

n = int(input())
a = list(map(int, input().split()))

mdc = a[0]
for i in range(1, n):
    mdc = gcd(mdc, a[i])

ans = 1
d = 2

while d * d <= mdc:
    cnt = 0
    while mdc % d == 0:
        cnt += 1
        mdc //= d

    if cnt:
        ans *= (cnt + 1)

    d += 1

if mdc > 1:
    ans *= 2

print(ans)