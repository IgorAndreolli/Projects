# Fatoração de Cholesky, usando fatores de cholesky

import numpy as np

'''Fatoração de Cholesky'''
# Descomentar para testar a matriz 3x3
A = np.array([[4, 1, 1],
              [1, 3, 1],
              [1, 1, 2]])

b = np.array([1, 0, -1], dtype=float)

# --------------------------------------
# Descomentar para testar a matriz 12x12

# A = np.array([
#     [31, 2, 4, 4, 3, 4, 2, 1, 2, 2, 2, 3],
#     [2, 36, 2, 2, 4, 3, 2, 3, 3, 5, 3, 4],
#     [4, 2, 32, 1, 4, 4, 2, 2, 4, 3, 2, 2],
#     [4, 2, 1, 34, 3, 3, 3, 4, 3, 2, 3, 2],
#     [3, 4, 4, 3, 38, 3, 1, 3, 3, 4, 2, 3],
#     [4, 3, 4, 3, 3, 40, 1, 2, 4, 4, 2, 4],
#     [2, 2, 2, 3, 1, 1, 29, 3, 3, 1, 3, 2],
#     [1, 3, 2, 4, 3, 2, 3, 35, 2, 5, 5, 3],
#     [2, 3, 4, 3, 3, 4, 3, 2, 34, 2, 1, 2],
#     [2, 5, 3, 2, 4, 4, 1, 5, 2, 38, 1, 3],
#     [2, 3, 2, 3, 2, 2, 3, 5, 1, 1, 31, 2],
#     [3, 4, 2, 2, 3, 4, 2, 3, 2, 3, 2, 32]
# ], dtype=float)

# b = np.array([220, 322, 294, 337, 399, 458, 356, 516, 469, 565, 493, 556], dtype=float)

# Verificando se a matriz A é simétrica e definida positiva

n = A.shape[0]
G = np.zeros_like(A, dtype=float)

for k in range(n):
    soma = 0
    for j in range(k):
        soma += G[k, j] ** 2
    r = A[k, k] - soma
    G[k, k] = np.sqrt(r)

    for i in range(k + 1, n):
        soma = 0
        for j in range(k):
            soma += G[i, j] * G[k, j]
        G[i, k] = (A[i, k] - soma) / G[k, k]


# multiplicador = G @ G.T
# # Verificando se a matriz A é igual ao produto de G e G transposta
# if np.allclose(A, multiplicador):   
#     Cholesky = True
# else:
#     Cholesky = False

# print(f"Matriz G*G.T:{G @ G.T}, A:{A}, G:{G}, Cholesky:{Cholesky}")  


# Resolvendo o sistema linear (G*G.Transpose)x = b  usando a fatoração de Cholesky
# i) Gy = b
# ii) G.T x = y
y = np.zeros(n, dtype=float)
x = np.zeros(n, dtype=float)

for k in range(n):
    s = 0
    for j in range(k):
        s += G[k][j] * y[j]
    y[k] = (b[k] - s) / G[k][k]

trans_G = G.T 
for k in range(n-1, -1, -1):
    s = 0
    for j in range(k+1, n):
        s += trans_G[k][j] * x[j]
    x[k] = (y[k] - s) / trans_G[k][k]


print(f"Resultado final y: {y}")
print(f"Resultado final x: {x}")