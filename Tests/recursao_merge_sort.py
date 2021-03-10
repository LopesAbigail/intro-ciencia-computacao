import pytest
# Recursão

def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista)//2

    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)

def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo: #Se for uma lista vazia
        return lado_direito

    if not lado_direito: #Se for uma lista vazia
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)

    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])
    

a = [4,8,7,4,1,3,5]
b = [7,2,6,4,5,5,7,0]
c = [3,1,1,2,5,4,4,3]
@pytest.mark.parametrize("lista, esperado", [
    (a, [1,3,4,4,5,7,8]),
    (b, [0,2,4,5,5,6,7,7]),
    (c, [1,1,2,3,3,4,4,5])
    ])
def testa_merge_sort(lista, esperado):
    assert merge_sort(lista) == esperado
