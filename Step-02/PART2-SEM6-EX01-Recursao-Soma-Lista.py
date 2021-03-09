''' Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de números inteiros e devolve um número inteiro correspondente à soma dos elementos desta lista.
 
    Sua solução deve ser implementada utilizando recursão.'''

def soma_lista(lista, posicao=-1, soma=0):
    tamanho_lista = len(lista)-1
    while posicao < tamanho_lista:
        posicao = posicao+1
        soma += lista[posicao]
        return soma_lista(lista, posicao, soma)
    return soma

lista = [1,2,3]

