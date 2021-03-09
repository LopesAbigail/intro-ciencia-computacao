def ordenada(lista):
    ''' Devolve True para lista ordenada e False caso contrário '''
    count = 0
    for i in range(len(lista)-1):
        if lista[i] < lista[i+1]:
            count += 1
    if count == len(lista)-1:
        return True
    else:
        return False
            
