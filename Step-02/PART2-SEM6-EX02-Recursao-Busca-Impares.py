def encontra_impares(lista):
    for elemento in lista:
        if elemento % 2 == 0:
            lista.remove(elemento)
            return encontra_impares(lista)
    return lista


'''(lista, posicao=-1, soma=0):
    tamanho_lista = len(lista)-1
    while posicao < tamanho_lista:
        posicao = posicao+1
        soma += lista[posicao]
        return soma_lista(lista, posicao, soma)
    return soma

lista = [1,2,3]


def encontra_impares(lista, lista_impar=[]):
    tamanho = len(lista)
    pares = []
    for i in range(tamanho):
        if lista[i] % 2 == 0:
            pares.append(lista[i])
        else:
            lista_impar.append(lista[i])
    print(lista_impar)


'''

