def ehPrimo(x):
    # fator = 2 pq 2 é o menor número utilizado na fatoração de números mais complexos
    fator = 2
    if(x == 2):
        return True
    
    while(x % fator and fator <= x/2):
        fator = fator + 1
    if(x % fator == 0):
        return False
    else:
        return True

limite = int(input("Insira o limite máximo: "))

n = 2
while n < limite:
    
    if (ehPrimo(n)):
        print(n, end=" , ")
    n = n +1
    
if(n <= 0):
    print("O número deve ser positivo e diferente de zero.")
