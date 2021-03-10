# Neasted loop - laços aninhados
# Tabuada X
linha = 1
coluna = 1

while(linha <= 10):
    while(coluna <= 10):
        print("{} X {} = ".format(linha, coluna), linha*coluna, end = " ")
        coluna = coluna + 1
    linha = linha + 1
    print()
    coluna = 1
