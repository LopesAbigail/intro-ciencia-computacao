#Sequência numérica terminada em 0 impressa ao contrário
n = 1
listaNumero = []
tamanho = len(listaNumero)

while n != 0:
    n = int(input("Número da sequência: "))
    listaNumero.append(n)

#Para inverter lista: listaNumero.reverse()
print(listaNumero)
