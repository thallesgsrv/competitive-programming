"""
PROGRESSÕES
"""

# ===== P.A. - PROGRESSÃO ARITMÉTICA =====
# An = A1 + (n - 1) * r
# Sn = n * (A1 + An) // 2

def pa_termo(A1, r, n):
    return A1 + (n - 1) * r

def pa_soma(A1, An, n):
    return n * (A1 + An) // 2

# ===== P.G. - PROGRESSÃO GEOMÉTRICA =====
# An = A1 * q**(n-1)
# Sn = A1 * (q**n - 1) // (q - 1)

def pg_termo(A1, q, n):
    return A1 * (q ** (n - 1))

def pg_soma(A1, q, n):
    if q == 1:
        return A1 * n
    return A1 * (q**n - 1) // (q - 1)

# ===== SOMATÓRIOS ESPECIAIS =====
def soma_n(n):
    return n * (n + 1) // 2

def soma_quadrados(n):
    return n * (n + 1) * (2*n + 1) // 6

def soma_cubos(n):
    return (n * (n + 1) // 2) ** 2
