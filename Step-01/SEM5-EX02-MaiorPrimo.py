def  maior_primo(x):

    def ehPrimo(num):
        aux = num
        numDivisores = 0

        while (0 < aux and aux <= num):
            if(num % aux == 0):
                numDivisores = numDivisores + 1
            aux = aux - 1

        if (numDivisores == 2):
            return True
        else:
            return False

    i = x
    while(0<i and i <= x):
        if ehPrimo(i):
            return i
        i = i - 1

