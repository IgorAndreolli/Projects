import numpy as np
import pandas as pd

'''Gauss-Jacobi''' 


A = np.array([
    [10, 2, 1],
    [1, 5, 1],
    [2, 3, 10]
], dtype=float)

b = np.array([7, -8, 6], dtype=float)



#criterio de convergencia Teorema (Critério das linas)
def convergencia(A):
    for i in range(len(A)):
        soma = 0
        for j in range(len(A)):
            if i != j:
                soma += abs(A[i][j])
        if abs(A[i][i]) <= soma:
            return False
    for i in range(len(A)):
        soma= 0
        for j in range(len(A)):
            if i != j:
                soma += A[i][j] / A[i][i]
        alfa = soma
        print(f"Alfa {i+1}: {alfa}")
    if alfa >= 1:
        return print("Critério de convergência não atendido. tente permutar a matriz A.")

    else:
        return print("Critério de convergência atendido.")
        
convergencia(A)

# pelo criterio de convergencia p valor de x(0) pode ser qualquer valor.
error = 5e-5  # Tolerância de erro
def gauss_jacobi(A, b):
    """ Implementação do metodo de Gauss-Jacobi """
    # Inicialização
    C = np.zeros_like(A, dtype=float)
    G =  np.zeros((3,1), dtype=float)
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                C[i][j] = 0
            else:
                C[i][j] = (-1*(A[i][j]) / A[i][i])
        G[i] = b[i] / A[i][i]
    return C, G

C, G = gauss_jacobi(A, b)

print(f"Matriz C: {C},\n Vetor G: {G}")