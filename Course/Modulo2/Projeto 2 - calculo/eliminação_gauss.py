import numpy as np
import pandas as pd

'''Eliminação de Gauss '''

# Exemplo de matriz aumentada para o sistema Ax = b
# Aqui, as três primeiras colunas são os coeficientes de A e a última coluna é o vetor b
matriz = np.array([
    [4, 1, 1],
    [1, 3, 1],
    [1, 1, 2]
], dtype=float)

matriz_resultado = np.zeros((3,3), dtype=float)
b = np.array([1, 0, -1], dtype=float)

#verificando o resultado 
x_ = np.linalg.solve(matriz, b)

# n = dimensão matriz
n = len(matriz)

for k in range(n):
    for i in range(k+1, n):
        
        a_ik = matriz[i][k]
        a_kk = matriz[k][k]
        m = a_ik/a_kk
        a_ik = 0
        for j in range(n):
            matriz[i][j] = matriz[i][j] - m * matriz[k][j]
        b[i] = b[i] - m * b[k]


print(f"Matriz resultado: {matriz},\n b: {b}") 

x = np.zeros(n, dtype=float)

for k in range(n-1, -1, -1):
    s = 0
    for j in range(k+1, n):
        s += matriz[k][j] * x[j]
    x[k] = (b[k] - s) / matriz[k][k]

print("---------------")
print(f"Resultado esperado: {x_}")
print("---------------")
print(f"Resultado obtido: {x}")