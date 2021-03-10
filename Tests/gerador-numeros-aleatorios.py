#Gerador de n numeros aleatórios
import random

def lista_grande(n):
    randomlist = []
    for i in range(n):
        num = random.randint(1,1000000000000)
        randomlist.append(num)
    return randomlist
