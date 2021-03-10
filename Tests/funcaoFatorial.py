#Função Fatorial

def fatorial(x):
    fatorial = 0

    if (x >= 0):
        i = x
        fatorial = 1
        if (x != 0):
            while (i <= x and i != 0):
                fatorial = fatorial * i
                i = i - 1

    return fatorial

def testFatorial():
    if(fatorial(1) == 1):
        print ("Método correto para x=1.")
    else:
        print ("Método incorreto para x=1.")
    if(fatorial(5) == 120):
        print ("Método correto para x=5.")
    else:
        print ("Método incorreto para x=5.")
    if(fatorial(0) == 1):
        print ("Método correto para x=0.")
    else:
        print ("Método incorreto para x=0.")
    if(fatorial(-5) == 0):
        print ("Método correto para x=-5.")
    else:
        print ("Método incorreto para x=-5.")
        
def numBinomial(n,k):
    if(k <= n):
        numBim = fatorial(n) // (fatorial(k)*fatorial(n-k))
        return numBim
    else:
        return "K deve ser menor ou igual a N."
    
