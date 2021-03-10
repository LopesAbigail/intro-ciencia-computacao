#POO
'''meu_carro = Carro()
carro_do_ime = Carro()

meu_carro.ano = 1968
meu_carro.modelo = "Fusca"
meu_carro.cor = "Light Blue"

carro_do_ime.ano = 1971
carro_do_ime.modelo = "Brasilia"
carro_do_ime.cor = "Yellow"

#Referência ao mesmo local da memória
novo_fusca = meu_carro
novo_fusca.ano += 10 #meu_carro.ano = 1978

# __init__ : Método construtor
'''

def main():
    carro1 = Carro('brasilia',1968,'amarela',80)
    carro2 = Carro('fuscão',1981,'preto',95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)

class Carro:
    def __init__(self, modelo, ano, cor, velocidade_maxima):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
        self.velocidade_maxima = velocidade_maxima

    def imprima(self):
        if(self.velocidade == 0): #Carro parado para ver o ano
            print("%s %s %d"%(self.modelo, self.cor, self.ano))
        elif(self.velocidade < self.velocidade_maxima):
            print("%s %s indo a %d Km/h"%(self.modelo, self.cor, self.velocidade))
        else:
            print("%s %s indo muuuuuito raaaaapiiiidoooo!"%(self.modelo, self.cor))
            
    def acelere(self, velocidade_aceleracao):
        self.velocidade = velocidade_aceleracao
        if(self.velocidade > self.velocidade_maxima):
            self.velocidade = self.velocidade_maxima
        self.imprima()

    def pare(self):
        self.velocidade = 0
        self.imprima()

main()
