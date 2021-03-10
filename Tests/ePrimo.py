num = int(input("Insira um número: "))
aux = num
numDivisores = 0

while (0 < aux and aux <= num):
    if(num % aux == 0):
        numDivisores = numDivisores + 1
    aux = aux - 1

if (numDivisores == 2):
    print("primo")
else:
    print("não primo")
