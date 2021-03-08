num = input('Insira um número: ')
quantDig = int(len(num))
num = int(num)
i = 0
soma = 0

while (i <= quantDig):
    soma = soma + (num % 10)
    num = num // 10
    i = i + 1
    
print(soma)
