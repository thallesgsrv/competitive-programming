def signature(s):
    stack = []
    for c in s:
        stack.append(c)
        if len(stack) >= 4 and stack[-4:] == ['(', 'x', 'x', ')']:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append('x')
            stack.append('x')
    return ''.join(stack)

T = int(input())
for _ in range(T):
    A = input()
    B = input()
    if signature(A) == signature(B):
        print("Yes")
    else:
        print("No")