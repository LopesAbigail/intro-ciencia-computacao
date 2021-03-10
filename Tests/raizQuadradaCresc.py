import math

a = int(input("Insira um valor para A: "))
b = int(input("Insira um valor para B: "))
c = int(input("Insira um valor para C: "))

delta = (b**2)-4*a*c

if (delta >= 0):
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    if (delta == 0):
        print("a raiz desta equação é",x1)
    else:
        if (x1>x2):
            print("as raízes da equação são",x2,"e",x1)
        else:
            print("as raízes da equação são",x1,"e",x2)
else:
    print("esta equação não possui raízes reais")
