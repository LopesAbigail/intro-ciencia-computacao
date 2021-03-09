# Dimensões da matriz

def dimensoes(matriz):
    ''' Inicializando a altura e a altura da matriz'''
    largura = 0
    altura = 0
    ''' Considerando que uma matriz é uma lista de listas
        Obtendo a quantidade de listas que há na lista principal (altura da matriz)
    '''
    for i in range(len(matriz)):
        '''' Verificando a quantidade de elementos que há em cada lista
             dentro da lista principal
        '''
        for j in range(len(matriz[i])):
            ''' Guardando 1 unidade a cada elemento encontrado
                descobrindo a largura da matriz
            '''
            largura = largura + 1
            ''' Indo para a próxima lista dentro da lista principal'''
            j = j + 1
        ''' Guardando 1 unidade para cada lista encontrada'''
        altura = altura + 1
        ''' Indo para a próxima'''
        i = i + 1
    print(str(i) + "X" + str(j))
