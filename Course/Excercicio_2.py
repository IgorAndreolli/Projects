

def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    return linhas, colunas


def soma_matrizes(m1, m2):
    linha_m1, coluna_m1 =  dimensoes(m1)
    linha_m2, coluna_m2 = dimensoes(m2)
    if linha_m1 ==linha_m2 and coluna_m1 ==coluna_m2:
        matriz_soma = [] 
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[0])):
                soma = (m1[i][j] + m2[i][j])
                linha.append(soma)
            matriz_soma.append(linha)
        resultado = matriz_soma
    else:
        resultado =  False

    return resultado

m1 =  [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7], [5 , 6, 7]]

matriz_soma = soma_matrizes(m1, m2)
print(matriz_soma)