meuCartao = int(input('Digite o número do cartão: '))

cartaoLido = 1
encontreiMeuCartaoNaLista = False

while (cartaoLido != 0 and not encontreiMeuCartaoNaLista):
    cartaoLido = int(input('Digite o número do próximo cartão: '))
    if (cartaoLido == meuCartao):
        encontreiMeuCartaoNaLista = True
        
if encontreiMeuCartaoNaLista:
    print('ENCONTRADO!')
else:
    print('NÃO ENCONTRADO')
