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

# This code is solving a problem where we have two integers `a` and `b`, and we need to determine the minimum number of operations required to make `a` and `b` equal by repeatedly dividing the larger number by 2. The code first checks if the larger number is divisible by the smaller number. If not, it prints -1, indicating that it's not possible to make them equal. If they are divisible, it calculates the ratio of the larger number to the smaller number and checks if this ratio is a power of 2. If it is a power of 2, it counts how many times we can divide the larger number by 2 until it becomes equal to the smaller number, and then calculates the minimum number of operations needed based on this count. If the ratio is not a power of 2, it prints -1, indicating that it's not possible to make them equal using the allowed operations.
# The logic behind this is that if the larger number can be reduced to the smaller number by dividing by 2, then the ratio of the larger to the smaller must be a power of 2. The number of times we need to divide by 2 corresponds to how many operations we need to perform, and since we can perform up to 3 operations in one step (dividing by 2 three times), we calculate the minimum number of steps required accordingly.
# The code reads multiple test cases, where each test case consists of two integers `a` and `b`. For each test case, it applies the logic described above and prints the result.