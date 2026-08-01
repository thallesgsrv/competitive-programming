"""
ENTRADA/SAÍDA RÁPIDA
"""

import sys
import math
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from functools import lru_cache
from itertools import combinations, permutations
import bisect

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# ===== LEITURA =====
n = int(input())                              # Um inteiro
a, b, c = map(int, input().split())          # Múltiplos inteiros
lista = list(map(int, input().split()))      # Lista de inteiros
s = input().strip()                           # String sem \n

# Matriz
n, m = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(n)]

# Múltiplos casos
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    # processa...

# Leitura até EOF
while True:
    try:
        linha = input().strip()
        if not linha:
            break
        n = int(linha)
        # processa...
    except EOFError:
        break

# ===== SAÍDA =====
out = []
out.append(str(resultado))
print("\n".join(out))
