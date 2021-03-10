# Imprimir matriz usualmente

def imprime_matriz(matriz):
    ''' Definindo o tamanho da(s) linha(s) e
        da(s) coluna(s) da matriz
    '''
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    for linha in range(linhas):
        ''' Inicializando contador para verificar
            quando imprimir ou não espaço entre os elementos
        '''
        count = 0
        if (linha != 0):
            print(end="\n")
        for coluna in range(colunas):
            matriz_usual = int(matriz[linha][coluna])
            count += 1
            if(colunas == count):
                print(matriz_usual, end="")
            else:
                print(matriz_usual, end=" ")
    print(end="\n")

    
