# Jogo do NIM
# Jogada do PC - Retorna um número de peças que seja múltiplo de (m+1)
def computador_escolhe_jogada(n, m):
    # Vez do computador:
    #print("\nVez do Computador\n")
    # Pode retirar todas as peças?
    if (n <= m):
        # Retira todas as peças e ganha o jogo:
        return n
    else:
        # Verifica se é possível deixar uma quantia múltipla de m+1:
        quantia = n % (m+1)
        if (quantia > 0):
            return quantia
        # Não é, então tirar m peças:
        return m

def usuario_escolhe_jogada(n, m):
    # Vez do usuário:
    #print("\nSua vez!")
    # Número de peças do usuário
    jogada = 0

    # Enquanto o número não for válido
    while (jogada == 0):
        jogada = int(input("\nQuantas peças você vai tirar? "))

    # Condições: jogada < n, jogada < m, jogada > 0
        if (jogada > n or jogada < 1 or jogada > m):
            print("\nOops! Jogada inválida! Tente de novo.")
            jogada = 0
    # Número de peças válido, retornar jogada
    return jogada 

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    # Verificar de quem é o turno
    e_turno_computador = True
    primeira_vez_usuario = False
    primeira_vez_computador = False

    # Decidir quem inicia o jogo
    if n % (m + 1) == 0:
        e_turno_computador = False
        primeira_vez_usuario = True
    else:
        primeira_vez_computador = True
    
    # Enquanto houver peças no tabuleiro
    while (n > 0):
        if(e_turno_computador):
            if(primeira_vez_computador):
                print("\nComputador começa!")
            primeira_vez_computador = False
            jogada = computador_escolhe_jogada(n, m)
            e_turno_computador = False
            print("Computador retirou {} peça(s).".format(jogada))
        else:
            if(primeira_vez_usuario):
                print("\nVoce começa!")
            primeira_vez_usuario = False
            jogada = usuario_escolhe_jogada(n, m)
            e_turno_computador = True
            print("Você retirou {} peça(s).".format(jogada))
        # Retirar as peças do jogo
        n = n - jogada

        if(n != 0):
            
            # Exibir estado atual do jogo
            print("Agora resta(m) apenas {} peça(s) no tabuleiro.".format(n))
        
    # Fim do jogo, verificar quem ganhou
    if(e_turno_computador):
        print("Fim de jogo! Você ganhou!")
        return 1
    else:
        print("Fim de jogo! O computador ganhou!")
        return 0

def campeonato():
    # Pontuações:
    usuario = 0
    computador = 0

    # Executa 3 vezes:
    for i in range(3):

        # Executa a partida:
        print("\n**** Rodada {} ****".format(i+1))
        vencedor = partida()

        # Verifica o resultado, somando a pontuação:
        if vencedor == 1:
            # Usuário venceu:
            usuario = usuario + 1
        else:
            # Computador venceu:
            computador = computador + 1

    # Exibe o placar final:
    print("\n**** Final do campeonato! ****")
    print("\nPlacar final: Você {} x {} Computador".format(usuario, computador))
    

print("Bem-vindo ao jogo do NIM! Escolha:")
numeroEhValido = False
# Validar o dígito do usuário
while(not numeroEhValido):
    escolha = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
    # Verificar modalidade escolhida
    if (escolha == 1):
        print("\nVocê escolheu uma partida isolada!")
        partida()
        numeroEhValido = True
    elif (escolha == 2):
        print("\nVocê escolheu um campeonato!")
        campeonato()
        numeroEhValido = True
