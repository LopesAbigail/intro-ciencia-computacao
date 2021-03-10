# exercicio recursao

def x(n):
    if n == 0:
        #<espaco a>
        print(n)
    else:
        #<espaço B>
        x(n-1)
        #<espaço C>
        print(n)
    #<espaço D>
#<espaço E>


def y(n, m):
    if n == m or m == 0:
        return 1
    else:
        return y(n-1,m) + y(n-1,m+1)
print(y(5,3))

def z(n):
    if n >= 0 and n <= 2:
        return n
    else:
        return z(n-1) + z(n-2) + z(n-3)
#print(z(6))

def busca_binaria(lista, elemento, min=0, max=None):
    cont = 0
    if max == None:
        max = len(lista)-1

    if max < min:
        return False
    else:
        meio = min + (max-min)//2

    if lista[meio] > elemento:
        cont += 1
        return busca_binaria(lista, elemento, min, meio - 1)
        
    elif lista[meio] < elemento:
        cont += 1
        return busca_binaria(lista, elemento, meio + 1, max)
    else:
        #print(cont)
        return meio







