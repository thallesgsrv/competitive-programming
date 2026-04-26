def main():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        maior, menor = max(a, b), min(a, b)
    
        if maior % menor != 0:
            print(-1)
            continue 
            
        diff = maior // menor
        
        if (diff & (diff - 1)) == 0:
            k = 0
            while diff > 1:
                diff >>= 1  
                k += 1
            
            print((k + 2) // 3)
        else:
            print(-1)

main()