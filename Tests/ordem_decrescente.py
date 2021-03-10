def ordenar(lista):
    lista_desc = []
    for pos in range(0,lista,-1):
        lista_desc.append(lista[pos])
    print (lista_desc)
