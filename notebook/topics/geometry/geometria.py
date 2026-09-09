"""
GEOMETRIA COMPUTACIONAL
"""

import math

# ===== DISTÂNCIAS =====
def dist_manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def dist_euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def dist2(p1, p2):  # sem raiz (mais rápido)
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

# ===== COLINEARIDADE =====
def colineares(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1)

# ===== DISTÂNCIA PONTO → RETA =====
# reta: (a, b, c) onde a*x + b*y + c = 0
def dist_ponto_reta(ponto, reta):
    x0, y0 = ponto
    a, b, c = reta
    return abs(a * x0 + b * y0 + c) / math.sqrt(a*a + b*b)

# ===== PONTO DENTRO DO CÍRCULO =====
def ponto_circulo(ponto, centro, raio):
    x, y = ponto
    cx, cy = centro
    d2 = (x - cx)**2 + (y - cy)**2
    r2 = raio**2
    if d2 < r2:
        return "dentro"
    elif d2 == r2:
        return "sobre"
    return "fora"

# ===== INTERSEÇÃO DE RETÂNGULOS =====
def intersecta_retangulos(r1, r2):
    (x1, y1), (x2, y2) = r1
    (x3, y3), (x4, y4) = r2
    return not (x2 < x3 or x4 < x1 or y1 < y4 or y3 < y2)

# ===== INTERSEÇÃO DE CÍRCULOS =====
def intersecao_circulos(c1, c2):
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    dx = x1 - x2
    dy = y1 - y2
    d2 = dx*dx + dy*dy
    soma = r1 + r2
    dif = abs(r1 - r2)

    if d2 == 0 and r1 == r2:
        return "coincidentes"
    if d2 > soma**2:
        return "sem intersecao"
    if d2 == soma**2:
        return "tangentes externas"
    if dif**2 < d2 < soma**2:
        return "duas intersecoes"
    if d2 == dif**2:
        return "tangentes internas"
    return "um dentro do outro"

# ===== ÁREA DO TRIÂNGULO =====
def area_triangulo(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)) / 2
