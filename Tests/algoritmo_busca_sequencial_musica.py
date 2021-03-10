#Busca Sequencial

class Musica:
    def __init__(self, titulo, interprete, compositor, ano):
        self.titulo = titulo
        self.interprete = interprete
        self.compositor = compositor
        self.ano = ano

class Buscador:
    def busca_por_titulo(self, seq, x):
        for i in range(len(seq)):
            if seq[i].titulo == x:
                return i
        return -1

    def vamos_buscar(self):
        playlist = [Musica("Ponta de Areia", "Milton Nascimento", "Milton Nascimento", 1975),
                    Musica("Podres Poderes", "Caetano Veloso", "Caetano Veloso", 1984),
                    Musica("Baby", "Gal Costa", "Caetano Veloso", 1969)]

        onde_achou = self.busca_por_titulo(playlist, "Baby")

        if(onde_achou == -1):
            print("A música buscada não está na playlist :(")
        else:
            preferida = playlist[onde_achou]
            print(preferida.titulo, preferida.interprete, preferida.compositor, preferida.ano,
                  sep = ', ');
