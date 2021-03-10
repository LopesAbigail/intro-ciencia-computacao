# Contar letras
'''
    (sting com a frase completa, padrão: "vogais" - mas aceita "consoantes")
'''

def conta_letras(frase, contar="vogais"):
    consoantes_ords = [98,99,100,102,103,104,106,107,108,109,110,112,113,114,
                       115,116,118,119,120,121,122]
    vogais_ords = [97,101,105,111,117]
    frase = frase.lower()
    cont_vogl = 0
    cont_cons = 0
    if(contar == "vogais"):
        for pos in range(len(frase)):
            for i in range(len(vogais_ords)):
                if(ord(frase[pos]) == vogais_ords[i]):
                    cont_vogl += 1
        return cont_vogl

    elif(contar == "consoantes"):
        for pos in range(len(frase)):
            for j in range(len(consoantes_ords)):
                if(ord(frase[pos]) == consoantes_ords[j]):
                    cont_cons += 1
        return cont_cons

    else:
        print("O último parâmtro deve ser 'vogais' ou 'consoantes'.")
