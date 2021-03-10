#Sequencia numerica inversa
n = 1
listaNumero = []

while n != 0:
    n = int(input("Número da sequência: "))
    listaNumero.append(n)
    #print("antes:", listaNumero)

tamanho = len(listaNumero) - 1
while tamanho >= 0:
    print(listaNumero[tamanho], end=", ")
    tamanho = tamanho - 1
