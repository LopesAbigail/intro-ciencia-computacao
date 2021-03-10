#maior elemento
def maior_elemento(lista):
    maior = -9999999999999999999999
    for obj in lista:
        if (obj > maior):
            maior = obj
    return maior
