# Retângulo
largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

for i in range(0, altura):
    for j in range(0, largura):
        if (i == 0 or i == altura-1 or j == 0 or j == largura-1): 
            print("#", end = "")
        else: 
            print(" ", end = "")
    print("")
    
