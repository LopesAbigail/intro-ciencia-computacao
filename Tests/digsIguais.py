num = int(input('Insira um número: '))
equal = False
anterior = num % 10
num = num // 10

while (num > 0 and not equal):
    atual = num % 10
    num = num // 10
    if(atual == anterior):
        equal = True
    anterior = atual
    
if equal:
    print('sim')
else:
    print('não')
