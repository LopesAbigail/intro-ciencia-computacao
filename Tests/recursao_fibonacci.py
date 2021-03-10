def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

'''
import pytest
# Recursão

def fibonacci(n):
    if n < 2: #Base da recursao
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) #Recursao em que fatorial(n) chama a si mesmo

@pytest.mark.parametrize("entrada, esperado", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    ])
def testa_fibonacci(entrada, esperado):
    assert fibonacci(entrada) == esperado

'''
