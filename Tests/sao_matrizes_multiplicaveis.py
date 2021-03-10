# Matrizes multiplicáveis

def sao_multiplicaveis(m1, m2):
    colunas_m1 = len(m1[0])
    linhas_m2 = len(m2)

    if(colunas_m1 == linhas_m2):
        #print("True")
        return True
    else:
        #print("False")
        return False
