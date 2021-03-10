# Fatorial

def fatorial(n):
    while True:
        #n = int(input("Insira o número desejado: "))
        if (n >= 0):
            i = n
            fatorial = 1
            if (n != 0):
                while (i <= n and i != 0):
                    fatorial = fatorial * i
                    i = i - 1
            return fatorial
        else:
            '''return "A função fatorial não admite números negativos, pois o resultado será sempre ZERO."'''
            return 0

import pytest
@pytest.mark.parametrize("entrada, valor_esperado",[
    (0,1),
    (1,1),
    (-10,0),
    (4,24),
    (5,120)
    ])

def testa_fatorial(entrada,valor_esperado):
    assert fatorial(entrada) == valor_esperado
