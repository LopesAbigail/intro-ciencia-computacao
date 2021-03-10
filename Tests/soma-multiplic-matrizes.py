#Operações com matrizes

import cria_matriz

#Soma
def soma_matrizes(a,b):
    num_linhas = len(a)
    num_colunas = len(a[0])
    c = cria_matriz.cria_matriz(num_linhas, num_colunas, 0)

    if(len(a) == len(b) and len(a[0]) == len(b[0])):
        #Percorrer linhas
        for line in range(num_linhas):
            #Percorrer colunas
            for column in range(num_colunas):
                c[line][column] = a[line][column] + b[line][column]
        return c
    else:
        print("Método funciona apenas com matrizes de mesmas dimensões!")

#Multiplicação
def multiplicacao_matrizes(a,b):
    num_linhas_a, num_col_a = len(a), len(a[0])
    num_linhas_b, num_col_b = len(b), len(b[0])
    assert num_col_a == num_linhas_b
    
    c = []

    #Percorrer linhas
    for line in range(num_linhas_a):
        #Começando nova linha
        c.append([])
        #Percorrer colunas
        for column in range(num_col_b):
            #Adicionando uma nova coluna
            c[line].append(0)
            for k in range(num_col_a):
                c[line][column] += a[line][k] * b[k][column]
    return c

if __name__ == '__main__':
    a = [[1,2,3],[4,5,6],[7,8,9]]
    b = [[10,20,30],[40,50,60],[70,80,90]]

    c = [[1,2,3],[4,5,6]]
    d = [[1,2],[3,4],[5,6]]
    #print(soma_matrizes(a,b))
    print(multiplicacao_matrizes(c,d))
