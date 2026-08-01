from collections import deque

# Imagine que cada número está ligado assim:
# 1 está ligado a 2 e 3
# 2 está ligado a 1 e 4
# 3 está ligado a 1 e 5
# 4 está ligado a 2
# 5 está ligado a 3

# Criando o grafo (lista de vizinhos)
grafo = {
    1: [2, 3],   # O número 1 tem vizinhos 2 e 3
    2: [1, 4],   # O número 2 tem vizinhos 1 e 4
    3: [1, 5],   # O número 3 tem vizinhos 1 e 5
    4: [2],      # O número 4 tem vizinho 2
    5: [3]       # O número 5 tem vizinho 3
}

def calcular_distancias(inicio):
    fila = deque([inicio])
    
    distancia = {inicio: 0}
    
    print(f"Começando BFS a partir do número {inicio}\n")
    
    while fila:
        atual = fila.popleft()
        print(f"Estou visitando o número {atual} (distância {distancia[atual]})")
        
        for vizinho in grafo[atual]:
            if vizinho not in distancia:
                distancia[vizinho] = distancia[atual] + 1
                fila.append(vizinho)
                print(f"  -> Descobri {vizinho} (distância {distancia[vizinho]})")
    
    print("\nDistancias finais:")
    for num, dist in distancia.items():
        print(f"  Número {num} está a {dist} passo(s) do número {inicio}")
    
    return distancia

distancias = calcular_distancias(1)