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