#Sequencia numerica inversa
n = 1
listaNumero = []
listaInversa = []

while n != 0:
    n = int(input("Número da sequência: "))
    listaNumero.append(n)

del(listaNumero[-1])

for obj in listaNumero[::-1]:
    #listaInversa.append(obj)
    print(obj)
