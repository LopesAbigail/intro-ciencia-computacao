class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if(self.a == self.b == self.c):
            return "equilátero"
        elif(self.a == self.b or self.a == self.c or self.c == self.b):
            return "isósceles"
        else:
            return "escaleno"

    def retangulo(self):
        if(self.a**2 == self.b**2 + self.c**2 or
           self.b**2 == self.a**2 + self.c**2 or
           self.c**2 == self.b**2 + self.a**2):
            return True
        else:
            return False

    def semelhantes(self, triangulo):
        list_self = []
        list_self.append(self.a)
        list_self.append(self.b)
        list_self.append(self.c)
        #list_self = list_self.sort(key = int)

        list_triangulo = []
        list_triangulo.append(triangulo.a)
        list_triangulo.append(triangulo.b)
        list_triangulo.append(triangulo.c)
        #list_triangulo = list_triangulo.sort(key = int)

        count = 0
        
        for item in range(len(list_self)):
            if(list_self[item] % list_triangulo[item] == 0):
                count += 1
        if(count == 3):
            return True
        else:
            return False
