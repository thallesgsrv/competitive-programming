"""
PROGRAMAÇÃO DINÂMICA (DP)
"""

# ===== TEMPLATE TOP-DOWN (MEMOIZATION) =====
def solve_topdown(n):
    memo = [-1] * (n + 1)

    def dp(estado):
        if estado == 0:
            return 1

        if memo[estado] != -1:
            return memo[estado]

        resultado = 0
        for opcao in opcoes:
            if estado - opcao >= 0:
                resultado += dp(estado - opcao)

        memo[estado] = resultado
        return resultado

    return dp(n)

# ===== TEMPLATE BOTTOM-UP (ITERATIVO) =====
def solve_bottomup(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for opcao in opcoes:
            if i - opcao >= 0:
                dp[i] += dp[i - opcao]

    return dp[n]

# ===== FIBONACCI =====
def fibonacci_topdown(n):
    memo = [-1] * (n + 1)
    memo[0] = 0
    memo[1] = 1

    def fib(x):
        if memo[x] != -1:
            return memo[x]
        memo[x] = fib(x-1) + fib(x-2)
        return memo[x]

    return fib(n)

def fibonacci_bottomup(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def fibonacci_otimizado(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# ===== DICE COMBINATIONS (CSES 1633) =====
def dice_combinations(n):
    MOD = 10**9 + 7
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for face in range(1, 7):
            if i - face >= 0:
                dp[i] = (dp[i] + dp[i - face]) % MOD

    return dp[n]
