#Busca Binária

# Busca em listas já ordenadas
# Eficiente! Boa complexidade computacional
def busca(lista_ord, x):
    # Pedaços do vetor, elementos
    # índice dos elementos
    primeiro = 0
    ultimo = len(lista_ord)-1
    
    elemento_existe = True

    # Ainda tem algum elemento dentro da sublista
    while primeiro <= ultimo:
        # índice do meio
        meio = (primeiro+ultimo)//2
        print(meio)
        if lista_ord[meio] == x:
            return meio
        else:
            if x < lista_ord[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    elemento_existe = False
    # Se o elemento não estiver na lista
    return elemento_existe

