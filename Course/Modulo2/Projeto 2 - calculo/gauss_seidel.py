
import numpy as np
import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-5):

    n = len(A)
    
    if x0 is None:
        x = np.zeros(n, dtype=float)
    else:
        x = x0.astype(float)
    
    flag = True
    iteracoes = 0

    while flag:
        x_old = x.copy()
        
        for i in range(n):
            soma = 0
            for j in range(n):
                if j != i:
                    soma += A[i, j] * x[j]
            x[i] = (b[i] - soma) / A[i, i]
        
        # Critério de parada 
        erro_relativo = np.max(np.abs(x - x_old)) / max(np.max(np.abs(x)), 1e-10)
        
        print(f"Iteração {iteracoes + 1}: x = {x}")
        
        if erro_relativo < tol:
            flag = False
        iteracoes += 1
    return x, iteracoes
# Exemplo de uso:
if __name__ == "__main__":

    # Descomente para testar a matriz 3x3
    # A = np.array([[4, 1, 1],
    #               [1, 3, 1],
    #               [1, 1, 2]], dtype=float)
    
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

    n = len(b)
    x0 = np.zeros(n, dtype=float)  # Chute inicial
    
    x_final, num_iter = gauss_seidel(A, b, x0, tol=1e-5)
    print(f"Solução final: {x_final}\n Número de iterações: {num_iter}")