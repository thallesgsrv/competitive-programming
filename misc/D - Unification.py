s = input().strip()

zeros = s.count('0')
uns = s.count('1')

print(2 * min(zeros, uns))