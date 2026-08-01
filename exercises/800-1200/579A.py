def main():
    num = int(input())
    cont = 0
    while num > 0:
        num &= (num-1)
        cont += 1
    print(cont)
main()

# This code is counting the number of set bits (1s) in the binary representation of a given integer `num`. It uses a common bit manipulation technique where `num & (num-1)` removes the lowest set bit from `num`, and the loop continues until `num` becomes 0. The count of iterations gives the number of set bits in the original integer. Finally, it prints the count of set bits.
# The logic behind this is that each time we perform `num & (num-1)`, we are effectively turning off the rightmost set bit in `num`. By counting how many times we can do this before `num` becomes 0, we can determine how many set bits were originally present in `num`.
# The code reads a single integer input, counts the number of set bits in its binary representation, and prints the result.
# For example, if the input is `5` (which is `101` in binary), the code will count 2 set bits and print `2`. If the input is `7` (which is `111` in binary), it will count 3 set bits and print `3`.