def main():
   for _ in range(int(input())):
    a,b,c = map(int, input().split())
    print(a^b^c)
main()

# This code is solving a problem where we have three integers `a`, `b`, and `c`, and we need to find the result of the bitwise XOR operation applied to these three integers. The code reads multiple test cases, where each test case consists of three integers. For each test case, it calculates the XOR of `a`, `b`, and `c` using the `^` operator and prints the result. The XOR operation will return a number that has bits set to 1 only in positions where an odd number of the input integers have bits set to 1.