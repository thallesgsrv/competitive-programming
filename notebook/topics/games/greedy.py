"""
MÉTODO GULOSO (GREEDY)
"""

# ===== PLANTAR FLORES (LEETCODE 605) =====
def can_place_flowers(flowerbed, n):
    planted = 0
    m = len(flowerbed)
    i = 0

    while i < m:
        if flowerbed[i] == 0:
            left_empty = (i == 0 or flowerbed[i-1] == 0)
            right_empty = (i == m-1 or flowerbed[i+1] == 0)

            if left_empty and right_empty:
                flowerbed[i] = 1
                planted += 1
                i += 2
                continue
        i += 1

    return planted >= n

# ===== TROCO DA LIMONADA (LEETCODE 860) =====
def lemonade_change(bills):
    cinco = 0
    dez = 0

    for nota in bills:
        if nota == 5:
            cinco += 1
        elif nota == 10:
            if cinco == 0:
                return False
            cinco -= 1
            dez += 1
        else:  # 20
            if dez >= 1 and cinco >= 1:
                dez -= 1
                cinco -= 1
            elif cinco >= 3:
                cinco -= 3
            else:
                return False
    return True

# ===== MÁXIMO DE FILMES (CSES 1629) =====
def max_filmes(filmes):
    filmes.sort(key=lambda x: x[1])
    resposta = 0
    fim_ultimo = 0

    for inicio, fim in filmes:
        if inicio >= fim_ultimo:
            resposta += 1
            fim_ultimo = fim

    return resposta

# ===== DRAGÕES (CODEFORCES 230A) =====
def derrotar_dragoes(s, dragoes):
    dragoes.sort()
    for forca, bonus in dragoes:
        if s <= forca:
            return "NO"
        s += bonus
    return "YES"
