arr = [1, 1, 2, 2, 3, 3, 4, 4, 5]    
slow = 0
    
for fast in range(1, len(arr)):
    if arr[fast] != arr[slow]:
        slow += 1
        arr[slow] = arr[fast]

print(slow + 1)

# This code is solving the problem of removing duplicates from a sorted array. The input array `arr` contains duplicate elements, and the goal is to modify the array in-place such that each element appears only once, and return the new length of the modified array.
# The code uses two pointers, `slow` and `fast`, to traverse the array. The `fast` pointer iterates through the array, while the `slow` pointer keeps track of the position of the last unique element found. Whenever a new unique element is encountered (i.e., when `arr[fast]` is not equal to `arr[slow]`), the `slow` pointer is incremented, and the unique element is moved to the position pointed to by `slow`. Finally, the code returns `slow + 1`, which represents the length of the modified array containing only unique elements.
