n = int(input())
count = 0
while n>0:
    n = n & (n-1)
    count += 1
print(count)

# This code counts the number of 1 bits in the binary representation of a given integer `n`. 
# It uses a loop that continues until `n` becomes zero. In each iteration, it performs a bitwise AND operation between `n` and `n-1`, which effectively removes the least significant 1 bit from `n`. 
# The count is incremented each time a 1 bit is removed. Finally, it prints the total count of 1 bits.