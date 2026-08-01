"""
TEORIA DOS JOGOS - NIM E GRUNDY
"""

# ===== JOGO DE NIM =====
def nim(pilhas):
    xor_total = 0
    for qtd in pilhas:
        xor_total ^= qtd
    return "first" if xor_total > 0 else "second"

# ===== MEX (MINIMUM EXCLUDED VALUE) =====
def mex(values):
    v = 0
    while v in values:
        v += 1
    return v

# ===== CALCULAR GRUNDY =====
def calcular_grundy(n, moves):
    grundy = [0] * (n + 1)

    for palitos in range(1, n + 1):
        alcancaveis = set()
        for take in moves:
            if take <= palitos:
                alcancaveis.add(grundy[palitos - take])
        grundy[palitos] = mex(alcancaveis)

    return grundy

# ===== GRUNDY OTIMIZADO =====
def calcular_grundy_otimizado(n, moves):
    moves = sorted(moves)
    grundy = [0] * (n + 1)
    seen = [False] * (n + 1)

    for palitos in range(1, n + 1):
        for take in moves:
            if take > palitos:
                break
            seen[grundy[palitos - take]] = True

        g = 0
        while seen[g]:
            g += 1
        grundy[palitos] = g

        for take in moves:
            if take > palitos:
                break
            seen[grundy[palitos - take]] = False

    return grundy

# ===== TEOREMA DE SPRAGUE-GRUNDY =====
def sprague_grundy(estados):
    """
    estados: lista de Grundy de cada subjogo
    """
    xor_total = 0
    for g in estados:
        xor_total ^= g
    return "first" if xor_total > 0 else "second"

# ===== EXEMPLO: JOGO DE STICK (CSES 1729) =====
n, k = map(int, input().split())
moves = list(map(int, input().split()))

grundy = calcular_grundy_otimizado(n, moves)

resultado = ""
for i in range(1, n + 1):
    resultado += "W" if grundy[i] > 0 else "L"

print(resultado)
