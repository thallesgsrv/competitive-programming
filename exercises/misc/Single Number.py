nums = map(int, input().split())
n = 0
for elem in nums: 
    n = n^elem
print(n)

# This code finds the single number in a list of integers where every element appears twice except for one.