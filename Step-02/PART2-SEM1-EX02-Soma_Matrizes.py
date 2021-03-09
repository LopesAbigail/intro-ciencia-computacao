# Soma matrizes

def dimensoes(matriz):
    largura = 0
    altura = 0
   
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            largura = largura + 1
            j = j + 1
        altura = altura + 1
        i = i + 1
    return str(i) + "X" + str(j)

def soma_matrizes(m1, m2):
    m_soma = []
    soma = 0
    if (dimensoes(m1) == dimensoes(m2)):
        for i in range(len(m1)):
            m_soma.append([])
            for j in range(len(m1[0])):
                soma = m1[i][j] + m2[i][j]
                m_soma[i].append(soma)
        print(m_soma)
    else:
        return False
