# Calcular maior e menor temperatura

def temperatura_minima(temperaturas):
    minima = temperaturas[0] # Inicializando com um valor que se tem certeza que existe na lista.
    i = 1 # Inicia com 1 porque "minima" já recebeu a posição 0 da lista "temperaturas"
    while i < len(temperaturas):
        if temperaturas[i] < minima:
            minima = temperaturas[i]
        i = i + 1
    return minima

def temperatura_maxima(temperaturas):
    maxima = temperaturas[0] # Inicializando com um valor que se tem certeza que existe na lista.
    i = 1 # Inicia com 1 porque "maxima" já recebeu a posição 0 da lista "temperaturas"
    while i < len(temperaturas):
        if temperaturas[i] > maxima:
            maxima = temperaturas[i]
        i = i + 1
    return maxima

def min_max_temperatura(listaTemperaturas):
    print("A menor temperatura do mês foi:", temperatura_minima(listaTemperaturas), "ºC.")
    print("A maior temperatura do mês foi:", temperatura_maxima(listaTemperaturas), "ºC.")

# Teste automatizado
def testa_temperatura_minima():
    print("Iniciando testes...")
    temp = [0]
    if(temperatura_minima(temp) != 0):
        print("Ocorreu um erro na lista ", temp)
    temp = [0, 0, 0, 0]
    if(temperatura_minima(temp) != 0):
        print("Ocorreu um erro na lista ", temp)
    temp = [0, 10, 80, 0, 22.5, -1]
    if(temperatura_minima(temp) != -1):
        print("Ocorreu um erro na lista ", temp)
    temp = [0, -15, -12, -1]
    if(temperatura_minima(temp) != 15):
        print("Ocorreu um erro na lista ", temp)
    print("Finalizando testes...")

# Refatorando o código de teste automatizado: eliminar código duplicado
# Extrair método
def verifica_temperatura_minima(temperaturas, temperatura_minima_esperada):
    temperatura_minima_encontrada = temperatura_minima(temperaturas)
    if(temperatura_minima_encontrada != temperatura_minima_esperada):
        print("Ocorreu um erro na lista ", temperaturas)
        print("O valor esperado era ", temperatura_minima_esperada,
              " - O valor encontrado foi ", temperatura_minima_encontrada)
# Chamando método para testes
def testa_temperatura_minima_refatorado():
    # Como chamar esses métodos de modo automatizado??
    verifica_temperatura_minima([0], 0)
    verifica_temperatura_minima([0, 0, 0, 0], 0)
    verifica_temperatura_minima([0, 10, 80, 0, 22.5, -1], -1)
    verifica_temperatura_minima([0, -15, -12, -1], -15)
