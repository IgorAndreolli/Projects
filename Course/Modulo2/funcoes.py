'''Multiplicação de matrizes'''



def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    return linhas, colunas

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2], [4], [1]]

linhas_m1, colunas_m1 = dimensoes(m1)
linhas_m2, colunas_m2 = dimensoes(m2)

print(f'{linhas_m1, colunas_m1}')
print(f'{linhas_m2, colunas_m2}')

if colunas_m1 == linhas_m2:
    matriz_multiplicada = []
    soma = 0
    for i in range(colunas_m1):
        linha = []
        for j in range(colunas_m1):
            produto = m1[i][j]*m2[j][i]
            soma +=produto
        linha.append(soma)
    matriz_multiplicada.append(linha)

    print(matriz_multiplicada)

else:
    print("Não é possivel multiplicar as matrizes")
