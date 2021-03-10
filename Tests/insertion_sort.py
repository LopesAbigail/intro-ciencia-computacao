# Insertion Sort

def insertion_sort(lista):
    i = 1
    while i < len(lista):
        j = i
        while j > 0 and lista[j-1] > lista[j]:
            lista[j], lista[j-1] = lista[j-1], lista[j]
            j -= 1
        i += 1
    return lista
