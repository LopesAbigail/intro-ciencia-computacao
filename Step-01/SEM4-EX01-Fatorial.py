num = int(input('Insira um número para calcular seu fatorial: '))
fatorial = 1
i = num

if (num != 0):
    while (i <= num and i != 0):
        fatorial = fatorial * i
        i = i - 1
else:
    fatorial = 1

print(fatorial)
