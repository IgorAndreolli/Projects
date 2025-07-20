import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def eliminacao_gauss(matriz, b):
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


    x = np.zeros(n, dtype=float)

    for k in range(n-1, -1, -1):
        s = 0
        for j in range(k+1, n):
            s += matriz[k][j] * x[j]
        x[k] = (b[k] - s) / matriz[k][k]

    return x

def grafico(x, y, alfa_1, alfa_2):

    # Ajuste de regressão linear (reta)
    coef = np.polyfit(x, y, 1)
    slope = alfa_2 
    intercept = alfa_1
    x = np.array(x)
    y = np.array(y)
    # Criação do gráfico de dispersão

    plt.scatter(x, y)

    # Adiciona a reta de regressão
    plt.plot(x, slope * x + intercept)

    # Insere a equação da reta no gráfico
    equation_text = f"y = {slope:.2f}x{intercept:.2f}"
    plt.annotate(equation_text, xy=(0.05, 0.95), xycoords='axes fraction',
                fontsize=12, va='top')

    # Rótulos
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfico de Dispersão com Reta de Regressão')

    # Exibe o gráfico
    plt.show()

def metodo(x_ano, y_nota):
        
    if len(x_ano) == len(y_nota):
        size = len(x_ano)
        print('Tamanho das listas coincidem')

    # formula de reta φ(x) = α1 + α2x,            onde g2(x) = x e g1(x) = 1
    matriz = np.zeros((2, 2))
    b = np.zeros(2)

    for i in range(2):
        for j in range(2):
            sum_a=0
            for n in range(size):
                if i == 0 and j == 0:
                    sum_a+= 1
                elif (i == 0 and j == 1) or (j == 0 and i == 1):
                    sum_a+= 1*x_ano[n]
                else:
                    sum_a+= (x_ano[n])**2
            print(f'Elemento a{i+1}{j+1} incluido na matriz')    
            matriz[i,j] = sum_a

        sum_b = 0
        for o in range(size):
            if i == 0:
                sum_b += y_nota[o]
            else:
                sum_b += x_ano[o]*y_nota[o]
        b[i] = sum_b
        print(f'elemento b{i+1}1')
    return matriz, b

if __name__ == '__main__':
    
    # Tabela_1 
    # ----------------------------------------------------
    x_tab1 = [2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023]
    y_tab1 = [4.9, 4.8, 5.8, 5.9, 6.0, 6.5, 6.7, 6.7, 6.2, 6.3]

    matriz, b = metodo(x_ano=x_tab1, y_nota=y_tab1)
    x = eliminacao_gauss(matriz, b)
    print(f'A função φ(x) = {x[1]}x {x[0]}')



    # Questão (b)
    alfa_1 = x[0]
    alfa_2 = x[1]
    # Descomentar caso queira avaliar o gráfico da tabela 1
    # grafico(x=x_tab1, y=y_tab1, alfa_1=alfa_1, alfa_2=alfa_2)
    resultado_tab1 = (6.8 - x[0])/x[1]
    print(f'o ano em que a nota será atingida para os ANOS INICIAIS é:{resultado_tab1}')
    # ---------------------------------------------------------------
    # Tabela_2 
    # ----------------------------------------------------
    x_tab2 = [2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023]
    y_tab2 = [4.4, 4.3, 4.6, 4.6, 4.7, 5.0, 5.2, 5.5, 5.5, 5.5]

    matriz, b = metodo(x_ano=x_tab2, y_nota=y_tab2)
    x = eliminacao_gauss(matriz, b)
    print(f'A função φ(x) = {x[1]}x {x[0]}')
    alfa_1 = x[0]
    alfa_2 = x[1]

    resultado_tab2 = (6.3 - x[0])/x[1]
    print(f'o ano em que a nota será atingida para os ANOS FINAIS é:{resultado_tab2}')
    # Comentar ou descomentar o gráfico
    grafico(x=x_tab2, y=y_tab2, alfa_1=alfa_1, alfa_2=alfa_2)