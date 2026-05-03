s = input().strip()
stack = []
for ch in s:
    if ch == 'B':
        if stack:
            stack.pop()
    else:
        stack.append(ch)
print(''.join(stack))


# This code processes a string `s` character by character. It uses a stack to keep track of the characters.
# When it encounters the character 'B', it checks if the stack is not empty and pops the last character from the stack. For any other character, it pushes it onto the stack.
# Finally, it joins the characters in the stack and prints the resulting string. This effectively simulates a backspace operation where 'B' represents a backspace that removes the last character entered.
