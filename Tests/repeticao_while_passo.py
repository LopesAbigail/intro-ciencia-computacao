#for

numeros = range(100, -1, -5) # inicio, fim, passo

for x in numeros:
    print(x)


cub_primos = [2 , 3 , 5 , 7 , 11 , 13 , 17 , 19 , 23 , 29 , 31 , 37]

for i in range(len(cub_primos)):
    cub_primos[i] = cub_primos[i]**3
print(cub_primos)
