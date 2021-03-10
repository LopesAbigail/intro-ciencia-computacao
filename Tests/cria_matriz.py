'''Matrizes'''

def cria_matriz(num_linhas, num_colunas, valor):
    '''(int, int, valor) --> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas, em que cada elemento é igual ao valor dado
    '''
    matriz = [] # Lista vazia
    for i in range(num_linhas):
        # Cria a linha i
        linha = [] # lista vazia
        for j in range(num_colunas):
            linha.append(valor)
        # Adiciona linha à matriz
        matriz.append(linha)

    return matriz

def le_matriz():
    '''(int, int, valor) --> matriz (lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas, em que cada elemento recebe cada valor inserido pelo teclado
    '''
    matriz = []
    num_linhas = int(input("Insira o número de linhas: "))
    num_colunas = int(input("Insira o número de colunas: "))
    
    for i in range(num_linhas):
    
        linha = []
        for j in range(num_colunas):
            valor = int(input("Insira o elemento[" + str(i) + "][" + str(j) + "]: "))
            linha.append(valor)
        
        matriz.append(linha)

    return matriz

def imprime_matriz_usualmente():
    pass
