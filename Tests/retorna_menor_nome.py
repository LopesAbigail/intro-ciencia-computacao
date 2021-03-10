''' Criar função que recebe lista com nomes de pessoas e retornar o menor
    Primeira letra maiúscula (capitalizado)
'''

def mais_curto(lista_de_nomes):
    atual = lista_de_nomes[0]
    for i in lista_de_nomes:
        if(len(atual.strip()) > len(i.strip())):
            atual = i
    #print(atual.strip().capitalize())
    return atual.strip().capitalize()

def retorna_lista_nomes_curtos(lista_de_nomes):

    print(min(lista_de_nomes))

def retorna_menor_order(lista):
    item_atual = lista[0]
    for item in lista:
        if(item_atual.lower() > item.lower()):
            item_atual = item
    return(item_atual.capitalize())

def testa_retorna_menor_order():
    #if(retorna_menor_order(["MACA","belize","anel"]) == "Anel"):
    print('Lista: ["MACA","belize","anel"]\n Esperado: Anel \n Encontrado: ' + retorna_menor_order(["MACA","belize","anel"]))
    #if(retorna_menor_order(["MACA","2Liz","anel"]) == "2Liz"):
    print('Lista: ["MACA","2Liz","anel"]\n Esperado: 2liz \n Encontrado: ' + retorna_menor_order(["MACA","2Liz","anel"]))
    #if(retorna_menor_order(["Fulize","belize","anel","1"]) == "1"):
    print('Lista: ["Fulize","belize","anel","1"]\n Esperado: 1 \n Encontrado: ' + retorna_menor_order(["Fulize","belize","anel","1"]))

def fazAlgo(string):
    pos = 0
    string1 = ""
    while pos < len(string):
        if string[pos] != " ":
            string1 = string1 + string[pos]
        pos = pos + 1
    return string1    

print(fazAlgo("É UM TESTE"))
