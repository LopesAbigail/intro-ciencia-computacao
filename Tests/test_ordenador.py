import ordenador
import pytest
import contatempo

class TestaOrdenador:

    @pytest.fixture
    def ordenad(self):
        return ordenador.Ordenador()

    @pytest.fixture
    def list_quase_ord(self):
        c = contatempo.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def list_aleatoria(self):
        c = contatempo.ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self, lista):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                return False
        return True
        
    def test_selecao_bolha_melhorada_aleatoria(self, ordenad, list_aleatoria):
        ordenad.selecao_bolha_melhorada(list_aleatoria)
        assert self.esta_ordenada(list_aleatoria)

    def test_selecao_direta_aleatoria(self, ordenad, list_aleatoria):
        ordenad.selecao_direta(list_aleatoria)
        assert self.esta_ordenada(list_aleatoria)

    def test_selecao_bolha_melhorada__quase_ord(self, ordenad, list_quase_ord):
        ordenad.selecao_bolha_melhorada(list_quase_ord)
        assert self.esta_ordenada(list_quase_ord)

    def test_selecao_direta_quase_ord(self, ordenad, list_quase_ord):
        ordenad.selecao_direta(list_quase_ord)
        assert self.esta_ordenada(list_quase_ord)

    
