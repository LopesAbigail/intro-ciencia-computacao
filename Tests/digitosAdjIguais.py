num = int(input('Digite o número: '))
encontreiDigAd = False
digAnterior = num % 10
num = num // 10

while (num > 0 and not encontreiDigAd):
    digAtual = num % 10
    num = num // 10
    if (digAnterior == digAtual):
        encontreiDigAd = True
    digAnterior = digAtual
        
if encontreiDigAd:
    print('sim')
else:
    print('não')
