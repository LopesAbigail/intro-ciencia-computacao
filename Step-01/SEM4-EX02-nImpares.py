num = int(input('Insira um número: '))
i = 0

while (i < num):
    if((2*i+1) % 2 != 0):
        impar = (2*i)+1 
        print(impar)
    else:
        print('erro')
    i = i + 1
