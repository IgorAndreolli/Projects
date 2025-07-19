import numpy as np
import pandas as pd
import sys
'''Gauss-Jacobi''' 


#criterio de convergencia Teorema (Critério das linhas)
def convergencia(A):

    for i in range(len(A)):
        soma= 0
        for j in range(len(A)):
            if i != j:
                soma += abs(A[i][j]) / A[i][i]
        alfa = soma
        print(f"Alfa {i+1}: {alfa}")
        if alfa >= 1:
            print(f"A matriz A não é convergente na alfa {i+1}")
    print("A matriz A é convergente")

def gauss_jacobi(A, b):
    """ Implementação do metodo de Gauss-Jacobi """
    # Inicialização
    C = np.zeros_like(A, dtype=float)
    G =  np.zeros_like(b, dtype=float)
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                C[i][j] = 0
            else:
                C[i][j] = (-1*(A[i][j]) / A[i][i])
        G[i] = b[i] / A[i][i]
    return C, G



if __name__ == "__main__":

    #Descomente para testar a matriz 3x3
    # A = np.array([
    #     [4, 1, 1],
    #     [1, 3, 1],
    #     [1, 1, 2]
    # ], dtype=float)

    # b = np.array([1, 0, -1], dtype=float)
    # Descomente para testar a matriz 12x12
    A = np.array([
        [31, 2, 4, 4, 3, 4, 2, 1, 2, 2, 2, 3],
        [2, 36, 2, 2, 4, 3, 2, 3, 3, 5, 3, 4],
        [4, 2, 32, 1, 4, 4, 2, 2, 4, 3, 2, 2],
        [4, 2, 1, 34, 3, 3, 3, 4, 3, 2, 3, 2],
        [3, 4, 4, 3, 38, 3, 1, 3, 3, 4, 2, 3],
        [4, 3, 4, 3, 3, 40, 1, 2, 4, 4, 2, 4],
        [2, 2, 2, 3, 1, 1, 29, 3, 3, 1, 3, 2],
        [1, 3, 2, 4, 3, 2, 3, 35, 2, 5, 5, 3],
        [2, 3, 4, 3, 3, 4, 3, 2, 34, 2, 1, 2],
        [2, 5, 3, 2, 4, 4, 1, 5, 2, 38, 1, 3],
        [2, 3, 2, 3, 2, 2, 3, 5, 1, 1, 31, 2],
        [3, 4, 2, 2, 3, 4, 2, 3, 2, 3, 2, 32]
    ], dtype=float)

    b = np.array([220, 322, 294, 337, 399, 458, 356, 516, 469, 565, 493, 556], dtype=float)



    convergencia(A)  # Verifica se a matriz A é convergente

    C, G = gauss_jacobi(A, b)
    error = 1e-5  # Tolerância de erro
    # calculo do vetor x

    #Descomente para testar a matriz 3x3
    # x = np.array([0.7, -1.6, 0.6], dtype=float) # x inicial Matriz 3x3
    x = np.array([-3 , 0.5, 6, 1, 3, 2, 4, 0.33, 0.18, 3, 20, 11], dtype=float)  # x inicial Matriz 12x12
    x_novo = np.zeros_like(b, dtype=float)

    iteracao = 0
    flag = True
    while flag:
        iteracao += 1
        print(f"Iteração {iteracao}")
        for i in range(len(A)):
            s = 0
            for j in range(len(A)):
                if i != j:
                    s += C[i][j] * x[j]
            x_novo[i] = G[i] + s    
        valores = []
        for i in range(len(C)):
            valor_ = abs(x_novo[i] - x[i])
            valores.append(valor_)
        if max(valores) / np.max(np.abs(x_novo)) < error:
            print(f"Convergência alcançada na iteração {iteracao}")
            flag = False
        else:
            x = x_novo.copy()
            print(f"Valores de x na iteração {iteracao}: {x_novo}")
        
    print(f"Resultado final: {x_novo}")
    print(f"Resultado esperado: {np.linalg.solve(A, b)}")