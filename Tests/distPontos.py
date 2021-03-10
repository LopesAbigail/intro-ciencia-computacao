#Distancia entre pontos
import math

x1 = int(input('Insira a coordenada X do P1: '))
y1 = int(input('Insira a coordenada Y do P1: '))
x2 = int(input('Insira a coordenada X do P2: '))
y2 = int(input('Insira a coordenada Y do P2: '))

distancia = math.sqrt(((x2-x1)**2)+((y2-y1)**2))

if (distancia >= 10):
    print('longe')
else:
    print("perto")
