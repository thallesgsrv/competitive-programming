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