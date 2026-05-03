def BitwiseAND(n, ns):
     num = ns[0]
     for i in range(1, n):
         num &= ns[i]
     return num

def main():
   for _ in range(int(input())):
      n = int(input())
      ns  = list(map(int, input().split()))
      print(BitwiseAND(n, ns))
main()

# This code defines a function `BitwiseAND` that takes an integer `n` and a list of integers `ns`. It initializes a variable `num` with the first element of the list `ns`, and then iteratively applies the bitwise AND operation with each subsequent element in the list. The final result is returned after processing all elements. 