s = input().strip()
stack = []
for ch in s:
    if ch == 'B':
        if stack:
            stack.pop()
    else:
        stack.append(ch)
print(''.join(stack))