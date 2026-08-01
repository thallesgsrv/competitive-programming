"""
BACKTRACKING
"""

# ===== TEMPLATE GERAL =====
def backtrack(estado, resultado):
    if solucao_completa(estado):
        resultado.append(estado[:])
        return

    for escolha in opcoes_possiveis(estado):
        if escolha_valida(escolha, estado):
            estado.append(escolha)
            backtrack(estado, resultado)
            estado.pop()

# ===== SUBCONJUNTOS (LEETCODE 78) =====
def subsets(nums):
    resultado = []

    def backtrack(start, caminho):
        resultado.append(caminho[:])
        for i in range(start, len(nums)):
            caminho.append(nums[i])
            backtrack(i + 1, caminho)
            caminho.pop()

    backtrack(0, [])
    return resultado

# ===== PERMUTAÇÕES (LEETCODE 46) =====
def permute(nums):
    resultado = []
    usado = [False] * len(nums)

    def backtrack(caminho):
        if len(caminho) == len(nums):
            resultado.append(caminho[:])
            return

        for i in range(len(nums)):
            if usado[i]:
                continue
            usado[i] = True
            caminho.append(nums[i])
            backtrack(caminho)
            caminho.pop()
            usado[i] = False

    backtrack([])
    return resultado

# ===== N-RAINHAS (LEETCODE 51) =====
def total_n_queens(n):
    def eh_valido(rainhas, linha, col):
        for l, c in rainhas:
            if linha == l or col == c:
                return False
            if abs(linha - l) == abs(col - c):
                return False
        return True

    def backtrack(rainhas, col):
        if col == n:
            return 1

        total = 0
        for linha in range(n):
            if eh_valido(rainhas, linha, col):
                rainhas.append((linha, col))
                total += backtrack(rainhas, col + 1)
                rainhas.pop()
        return total

    return backtrack([], 0)
