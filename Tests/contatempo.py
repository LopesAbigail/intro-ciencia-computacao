import ordenador
import random
import time
import algoritmos_busca

class ContaTempos:

    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)] # Inteiros aleatórios entre 0 e 999
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)] # Lista de 0 a n-1
        lista[n//10] = -500 # Inserindo um número fora de ordem
        return lista

    def compara_busca(self, n, obj):
        lista1 = [x for x in range(n)] # Lista Ordenada
        lista2 = lista1[:]

        b = algoritmos_busca.Buscador()

        print("Comparando buscas")
        antes = time.time()
        b.busca_binaria(lista1, obj)
        depois = time.time()
        print("O método busca_binaria() consumiu",depois - antes,"s")

        antes = time.time()
        b.busca_sequencial(lista1, obj)
        depois = time.time()
        print("O método busca_sequencial() consumiu",depois - antes,"s")


    def compara_ordenacao(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:] # Clonando a lista1, outra lista mas com conteúdo igual

        o = ordenador.Ordenador()

        print("Comparando com listas aleatórias")
        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("O método selecao_direta() consumiu",depois - antes,"s")
        
        antes = time.time()
        o.selecao_bolha(lista1)
        depois = time.time()
        print("O método selecao_bolha() consumiu",depois - antes,"s")

        print("\nComparando com listas quase ordenadas")
        lista1 = self.lista_quase_ordenada(n)
        antes = time.time()
        o.selecao_direta(lista1)
        depois = time.time()
        print("O método selecao_direta() consumiu",depois - antes,"s")

        lista2 = lista1[:]
        antes = time.time()
        o.selecao_bolha_melhorada(lista2)
        depois = time.time()
        print("O método selecao_bolha_melhorada() consumiu",depois - antes,"s")
