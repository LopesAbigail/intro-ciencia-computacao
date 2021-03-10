def clone(lista):
    clone = []
    for objeto in lista:
        clone.append(objeto)
    return clone
    
# metodo nativo para criar clone: lista2 = lista1[:]
# fatiar lista = lista1[3:5]
# "objeto" in lista1 => retorna True or False
# Concatenar: [1,2] + [3,4]
# b = [1,2] -> b = b * 5 -> [1,2,1,2,1,2,1,2,1,2]
# Remoção -> a = [1,2,3] -> del a[1] -> [1,3] (apaga item ou trecho da lista)
