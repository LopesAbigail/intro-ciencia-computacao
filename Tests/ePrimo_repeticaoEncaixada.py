def ehPrimo(n):
    # fator = 2 pq 2 é o menor número utilizado na fatoração de números mais complexos
    fator = 2
    while(n % fator and fator <= n/2):
        fator = fator + 1
    if(n % fator == 0):
        return False
    else:
        return True

num = int(input("Insira um número natural: "))

while num > 0:
    
    if (ehPrimo(num)):
        print(num,"é primo")
    else:
        print(num,"não é primo")
    num = int(input("Insira um número: "))
    
if(num <= 0):
    print("O número deve ser positivo e diferente de zero.")
