numbers = [1, 2, 3, 4, 4, 9, 56, 90]
target = 8 
nums = [] 

low = 0
high = len(numbers) - 1

while low < high: 
    sum = numbers[low] + numbers[high]
    if sum == target:
        nums.append(low + 1)
        nums.append(high + 1)
        break
    elif sum < target:
        low += 1
    else:
        high -= 1 
print(nums)

# This code is solving the "Two Sum II - Input Array Is Sorted" problem. The goal is to find two numbers in a sorted array that add up to a specific target. The code uses a two-pointer approach, where one pointer starts at the beginning of the array (low) and the other pointer starts at the end of the array (high).