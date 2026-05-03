n = int(input())
balls = list(map(int, input().split())) 

stack = []
tamanho = 0 

for ball in balls:
    if stack and stack[-1][0] == ball:
        contagem = stack[-1][1] + 1
        stack[-1] = (ball, contagem)
        tamanho += 1
        if contagem == ball:
            tamanho -= ball
            stack.pop()
    else:
        stack.append((ball, 1))
        tamanho += 1        
    print(tamanho)

# This code simulates a game where you have a stack of balls, and each ball has a number on it. When you add a ball to the stack, if the top ball has the same number, you increase the count of that number. If the count reaches the number on the ball, you remove all those balls from the stack. The variable `tamanho` keeps track of the total number of balls in the stack at any given time, and it is updated accordingly when balls are added or removed. After processing each ball, it prints the current size of the stack.
# The input consists of an integer `n` representing the number of balls, followed by a list of integers representing the numbers on the balls. The code iterates through each ball, updates the stack and the size, and prints the size after each ball is processed.
