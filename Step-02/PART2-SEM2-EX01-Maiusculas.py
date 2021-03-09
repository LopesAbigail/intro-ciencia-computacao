# Letras maiúsculas

# Imprimir em ordem alfebética
'''def maiusculas(frase):
    letras_maiusculas = ""
    list_ords_maiusculos = [
        65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90
        ]
    pos = len(frase)-1
    while pos >= 0:
        for vez in range(0,len(list_ords_maiusculos)):
            if(ord(frase[pos]) == list_ords_maiusculos[vez]):
                letras_maiusculas += frase[pos]
        pos -= 1
    return letras_maiusculas
'''
# Imprimir na ordem em que as letras aparecem
'''def maiusculas(frase):
    letras_maiusculas = ""
    tamanho = len(frase)-1
    for pos in range(tamanho):
        if(ord(frase[pos]) == 65 or ord(frase[pos]) == 66 or ord(frase[pos]) == 67 or
         ord(frase[pos]) == 68 or ord(frase[pos]) == 69 or ord(frase[pos]) == 70 or ord(frase[pos]) == 71 or
         ord(frase[pos]) == 72 or ord(frase[pos]) == 73 or ord(frase[pos]) == 74 or ord(frase[pos]) == 75 or
         ord(frase[pos]) == 76 or ord(frase[pos]) == 77 or ord(frase[pos]) == 78 or ord(frase[pos]) == 79 or
         ord(frase[pos]) == 80 or ord(frase[pos]) == 81 or ord(frase[pos]) == 82 or ord(frase[pos]) == 83 or
         ord(frase[pos]) == 84 or ord(frase[pos]) == 85 or ord(frase[pos]) == 86 or ord(frase[pos]) == 87 or
         ord(frase[pos]) == 88 or ord(frase[pos]) == 89 or ord(frase[pos]) == 90):
            letras_maiusculas += frase[pos]
    return letras_maiusculas
'''
# Imprimir na ordem em que as letras aparecem (com lista)
def maiusculas(frase):
    letras_maiusculas = ""
    list_ords_maiusculos = [
        65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90
        ]
    tamanho = len(frase)
    for pos in range(0,tamanho):
        for vez in range(len(list_ords_maiusculos)):
            if(ord(frase[pos]) == list_ords_maiusculos[vez]):
                letras_maiusculas += frase[pos]
    return letras_maiusculas
