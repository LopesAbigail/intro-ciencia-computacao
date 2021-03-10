# Algoritmo de Ordenação Seleção Direta

class Ordenador:
    
    #Seleção direta
    ''' A cada passo busca o menor elemento e o coloca na posição inicial '''
    def selecao_direta(self, lista):
        fim = len(lista)

        for i in range(fim - 1):
            # Inicialmente, o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            # Coloca o menor elemento encontrado no início da sublista
            # Para isso, troca de lugar os elementos nas posições i e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]
            
    ''' Percorre todo o vetor fazendo a troca de elementos adjacentes'''
    def selecao_bolha(self, lista):
        fim = len(lista)

        # Começo a percorrer pelo fim do vetor
        # A cada passagem, decubro o "mais pesado" e jogo para o final do vetor
        for i in range(fim-1, 0 , -1):
            # Percorrendo todo o vetor e fazendo a troca dos elementos adjacentes
            # que estão fora de ordem
            # Desde a posição 0 até a posição i-1
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    ''' Algoritmo com desempenho melhorado'''
    def selecao_bolha_melhorada(self, lista):
        fim = len(lista)

        # Começo a percorrer pelo fim do vetor
        # A cada passagem, decubro o "mais pesado" e jogo para o final do vetor
        for i in range(fim-1, 0 , -1):
            # Detectar se o algoritmo é executado sem ter realizado alguma traca de elementos adjacentes
            trocou = False
            # Percorrendo todo o vetor e fazendo a troca dos elementos adjacentes
            # que estão fora de ordem
            # Desde a posição 0 até a posição i-1
            for j in range(i):
                if lista[j] > lista[j+1]:
                    # Linha em que ocorre a troca de elementos
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            if not trocou:
                return

    def insertion_sort(self, lista):
        fim = len(lista)

        for i in range(fim):
            index = lista[i]
            j = i
            while(j > 0 and lista[j-1] > index):
                lista[j] = lista[i-1]
                j = j - 1
            lista[j] = index
        return lista

