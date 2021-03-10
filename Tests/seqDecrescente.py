decrescente = True
anterior = int(input('Primeiro número: '))
valor = 1

while(valor != 0 and decrescente):
    valor = int(input("Próximo número: "))
    if (valor >= anterior):
        decrescente = False
    anterior = valor
    
if decrescente:
    print("A sequênca está em ordem decrescente!")
else:
    print("A sequênca não está em ordem decrescente!")
