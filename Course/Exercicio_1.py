
'''Tamanho da matriz'''
def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    return print(f'{linhas}X{colunas}')

matriz = [[1, 2, 3], [4, 5, 6]]
dimensoes(matriz)