def incomodam(n, indice=0, string=""):
    if(n > 0):
        while n > indice:
            string += "incomodam "
            indice = indice+1
            return incomodam(n, indice, string)
    return string

def elefantes(n, letra='', frase_inicial='Um elefante incomoda muita gente\n',i=2):
    while(n > 1 and n >= i):
        letra = letra + frase_inicial
        letra = letra + str(i) + " elefantes " + incomodam(i) + "muito mais\n"
        frase_inicial = str(i) + " elefantes incomodam muita gente\n"
        i = i+1
        return elefantes(n, letra, frase_inicial, i)
    return letra
