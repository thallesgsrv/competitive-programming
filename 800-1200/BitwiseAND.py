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