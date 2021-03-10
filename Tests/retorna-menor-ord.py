'''
	Criar método que recebe uma lista de strings e retorna a que possui a 1
	letra com o menor .order()
	Considerar letras maiusculas e minusculas
'''	
def primeiro_lex(lista):
    item_atual = lista[0]
    for item in lista:
        if(ord(item_atual[0]) > ord(item[0])):
            item_atual = item
    return(item_atual)
