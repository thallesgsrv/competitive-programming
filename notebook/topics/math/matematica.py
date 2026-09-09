"""
MATEMÁTICA BÁSICA
"""

import math

# ===== MDC / MMC =====
mdc = math.gcd(a, b)                 # Máximo Divisor Comum
mmc = a * b // math.gcd(a, b)        # Mínimo Múltiplo Comum

# ===== PRIMO =====
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# ===== CRIVO DE ERATÓSTENES =====
def crivo(n):
    primos = [True] * (n + 1)
    primos[0] = primos[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primos[i]:
            for j in range(i * i, n + 1, i):
                primos[j] = False
    return [i for i in range(n + 1) if primos[i]]

# ===== FATORAÇÃO =====
def fatoracao(n):
    fatores = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            fatores.append(d)
            n //= d
        d += 1
    if n > 1:
        fatores.append(n)
    return fatores

# ===== EXPONENCIAÇÃO RÁPIDA =====
def exp_rapida(base, exp, mod=10**9+7):
    res = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return res
