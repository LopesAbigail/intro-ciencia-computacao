# WHILE
digitados = int(input('Insira o tamanho da sequencia: '))
soma = 0
produto = 1
aux = 0

while(aux < digitados):
    valor = int(input('Digite o valor: '))
    soma = soma + valor
    produto = produto * valor
    aux = aux + 1

print('A soma é:', soma)
print('O produto é:', produto)
