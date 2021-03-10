import pytest
# Recursão

def busca_binaria_recursiva(lista, elemento, elemento_min=0, elemento_max=None):
    if elemento_max == None:
        elemento_max = len(lista)-1 # the last lists element 

    if elemento_max < elemento_min:
        return False #Elemento nao esta na lista
    else:
        meio = elemento_min + (elemento_max-elemento_min)//2 #Buscar nos meios

    if lista[meio] > elemento:
        return busca_binaria_recursiva(lista, elemento, elemento_min, meio-1)
    elif lista[meio] < elemento:
        return busca_binaria_recursiva(lista, elemento, meio+1, elemento_max)
    else:
        return meio # Se achou o elemento no meio, retorna o indice do meio

a = [10,20,30,40,50,60]
@pytest.mark.parametrize("lista, valor, esperado", [
    (a, 10, 0),
    (a, 20, 1),
    (a, 30, 2),
    (a, 40, 3),
    (a, 50, 4),
    (a, 70, False),
    (a, 15, False),
    (a, -10, False)
    ])
def testa_busca_binaria_recursiva(lista, valor, esperado):
    assert busca_binaria_recursiva(lista, valor) == esperado
