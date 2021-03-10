import math

a = int(input("Insira um valor para A: "))
b = int(input("Insira um valor para B: "))
c = int(input("Insira um valor para C: "))

delta = (b**2)-4*a*c

if (delta >= 0):
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    if (delta == 0):
        print("A equação possui apenas uma raiz real, que é",x1,"\nDelta =",delta)
    else:
        print("A equação possui duas raízes reais, que são:",x1,"e",x2,"\nDelta =",delta)
else:
    print("A equação não possui raízes reais.\nDelta =",delta)
