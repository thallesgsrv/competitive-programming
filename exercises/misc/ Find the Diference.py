s, t = input().split()
xor = 0

for let in s:
    xor ^= ord(let)
for let in t:
    xor ^= ord(let)
print(chr(xor))

# This code is finding the character that is present in one of the two input strings `s` and `t`, but not in both. It does this by using the XOR operation on the ASCII values of the characters in both strings. The XOR operation will cancel out characters that are present in both strings, leaving only the character that is unique to one of the strings. Finally, it converts the resulting ASCII value back to a character and prints it.