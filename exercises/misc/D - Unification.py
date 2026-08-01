s = input().strip()

zeros = s.count('0')
uns = s.count('1')

print(2 * min(zeros, uns))

# This code counts the number of '0's and '1's in the input string `s`. It then calculates the minimum of these two counts and multiplies it by 2 to determine the maximum length of a substring that can be formed by removing characters from `s` such that the substring contains an equal number of '0's and '1's. The result is printed as the output.
