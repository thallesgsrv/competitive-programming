def main():
    a,b = map(int, input().split())
    print(a^b)
main()

# This code reads two integers `a` and `b` from the input, computes their bitwise XOR using the `^` operator, and prints the result. The bitwise XOR operation compares each bit of the two numbers and returns a new number where each bit is set to 1 if the corresponding bits of the operands are different, and 0 if they are the same.
