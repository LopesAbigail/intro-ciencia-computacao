#Busca Sequencial
class Buscador:
    
    def busca_sequencial(self, seq, x):
        ''' (list, float) -> float '''
        for i in range(len(seq)):
            if seq[i] == x:
                return True
        return False

    # Busca em listas já ordenadas
    # Eficiente! Boa complexidade computacional
    def busca_binaria(self, lista_ord, x):
        esta_ordenada = False
        for i in range(len(lista_ord)-1):
            if lista_ord[i] < lista_ord[i+1]:
                esta_ordenada = True
            else:
                esta_ordenada = False

        if esta_ordenada:
            # Pedaços do vetor, elementos
            # índice dos elementos
            primeiro = 0
            ultimo = len(lista_ord)-1

            # Ainda tem algum elemento dentro da sublista
            while primeiro <= ultimo:
                # índice do meio
                meio = (primeiro+ultimo)//2
                if lista_ord[meio] == x:
                    return meio
                else:
                    if x < lista_ord[meio]:
                        ultimo = meio - 1
                    else:
                        primeiro = meio + 1
                        
            # Se o elemento não estiver na lista
            return -1
