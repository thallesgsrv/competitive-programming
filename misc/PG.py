def soma_pg(a1, n, q):
    if n <= 0:
        return "Erro: n deve ser positivo"
    if q == 1:
        return n * a1
    return (a1 * (q**n - 1)) / (q - 1)

print(soma_pg(1, 4, 2)) 
print(soma_pg(3, 5, 2))    
print(soma_pg(5, 3, 1))    
print(soma_pg(100, 3, 0.5)) 