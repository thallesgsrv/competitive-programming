"""
ESTRUTURAS DE DADOS
"""

from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
import bisect

# ===== FILA (BFS) =====
fila = deque([1, 2, 3])
fila.append(4)        # insere no final
x = fila.popleft()    # remove do início O(1)

# ===== PILHA (DFS) =====
pilha = [1, 2, 3]
pilha.append(4)       # insere no topo
x = pilha.pop()       # remove do topo O(1)

# ===== FILA DE PRIORIDADE (HEAP) =====
heap = []
heappush(heap, 5)
heappush(heap, 1)
heappush(heap, 3)
x = heappop(heap)     # remove o menor → 1

# ===== DICIONÁRIO / MAPA =====
d = defaultdict(int)          # valor padrão 0
d = defaultdict(list)         # valor padrão []
d['chave'] = 10
print(d['chave'])             # 10
print(d['inexistente'])       # 0

# ===== CONTADOR =====
arr = [1, 2, 2, 3, 3, 3]
freq = Counter(arr)           # Counter({3: 3, 2: 2, 1: 1})
print(freq[2])                # 2

# ===== CONJUNTO =====
s = set([1, 2, 3])
s.add(4)                      # insere
s.remove(4)                   # remove (erro se não existir)
s.discard(4)                  # remove (não erro)
if 2 in s:                    # busca O(1)
    pass

# ===== BISECT (BUSCA BINÁRIA) =====
arr = [1, 3, 5, 7, 9]
pos = bisect.bisect_left(arr, 5)   # 2
pos = bisect.bisect_right(arr, 5)  # 3
bisect.insort(arr, 6)              # insere mantendo ordem
