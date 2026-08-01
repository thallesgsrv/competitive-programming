n = int(input())
arr = []
for i in range(n+1):
    count = 0
    while i > 0: 
        i = i & (i-1)
        count += 1
    arr.append(count)
print(arr)

# This code is counting the number of set bits (1s) in the binary representation of each integer from 0 to `n`. It uses a common bit manipulation technique where `i & (i-1)` removes the lowest set bit from `i`, and the loop continues until `i` becomes 0. The count of iterations gives the number of set bits in the original integer. The results are stored in an array `arr`, which is printed at the end.