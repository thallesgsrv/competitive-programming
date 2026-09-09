"""
ANÁLISE COMBINATÓRIA
"""

import math
from itertools import combinations, permutations

# ===== FATORIAL =====
math.factorial(n)

# ===== ARRANJO (ORDEM IMPORTA) =====
# An,p = n! / (n-p)!
def arranjo(n, p):
    return math.factorial(n) // math.factorial(n - p)

# ===== COMBINAÇÃO (ORDEM NÃO IMPORTA) =====
# Cn,p = n! / (p! * (n-p)!)
def combinacao(n, p):
    return math.comb(n, p)  # Python 3.8+

# Implementação manual
def comb(n, p):
    p = min(p, n - p)
    res = 1
    for i in range(1, p + 1):
        res = res * (n - p + i) // i
    return res

# ===== PERMUTAÇÃO COM REPETIÇÃO =====
# P = n! / (a! * b! * c!...)
def permutacao_com_rep(n, repeticoes):
    res = math.factorial(n)
    for r in repeticoes:
        res //= math.factorial(r)
    return res

# ===== GERAR COMBINAÇÕES/PERMUTAÇÕES =====
for c in combinations([1,2,3,4], 2):
    print(c)  # (1,2), (1,3), (1,4), (2,3), ...

for p in permutations([1,2,3], 2):
    print(p)  # (1,2), (1,3), (2,1), ...
