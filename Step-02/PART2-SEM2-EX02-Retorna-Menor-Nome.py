''' Criar função que recebe lista com nomes de pessoas e retornar o menor
    Primeira letra maiúscula (capitalizado)
'''

def menor_nome(lista_de_nomes):
    atual = lista_de_nomes[0]
    for i in lista_de_nomes:
        if(len(atual.strip()) > len(i.strip())):
            atual = i
    #print(atual.strip().capitalize())
    return atual.strip().capitalize()


