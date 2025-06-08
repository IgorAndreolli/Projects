import datetime  as dt
import pandas as pd
import numpy as np



def my_matrix(matriz):
    for i in matriz:
        linhas = len(matriz)
        colunas = len(i)

    return print(f'{linhas}X{colunas}')

matriz = [[1, 2, 3], [4, 5, 6]]
my_matrix(matriz)