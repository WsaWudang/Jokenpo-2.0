import random

# Define as opções de jogadas
jogadas = ['pedra', 'papel', 'tesoura']

# Função para determinar o vencedor
def determinar_vencedor(jogador1, jogador2):
    if jogador1 == jogador2:
        return 'empate'
    elif jogador1 == 'pedra' and jogador2 == 'tesoura':
        return 'jogador1'
    elif jogador1 == 'papel' and jogador2 == 'pedra':
        return 'jogador1'
    elif jogador1 == 'tesoura' and jogador2 == 'papel':
        return 'jogador1'
    else:
        return 'jogador2'

# Função para jogar contra o computador
def jogar_contra_computador():
    jogador1_vitorias = 0
    computador_vitorias = 0
    
    jogador1 = input("\nDigite o nome do jogador 1: ")
    jogador2 = 'PC'
    
    while jogador1_vitorias < 3 and computador_vitorias < 3:
        jogador1_jogada = input(f"{jogador1}, digite sua jogada (pedra, papel ou tesoura): ")
        
        while jogador1_jogada != 'pedra' and jogador1_jogada != 'papel' and jogador1_jogada != 'tesoura':
            print("Entrada inválida! Por favor, digite uma jogada válida (pedra, papel ou tesoura).")
            jogador1_jogada = input(f"{jogador1}, digite sua jogada (pedra, papel ou tesoura): ")

        computador_jogada = random.choice(jogadas)
        print(f"O computador jogou: {computador_jogada}")
        vencedor = determinar_vencedor(jogador1_jogada, computador_jogada)
        
        if vencedor == 'jogador1':
            jogador1_vitorias += 1
            print(f"{jogador1} venceu a rodada!")
        elif vencedor == 'jogador2':
            computador_vitorias += 1
            print("O computador venceu a rodada!")
        else:
            print("Empate!")
            
        print(f"Placar atual: {jogador1} - {jogador1_vitorias} x {computador_vitorias} - Computador\n")
    
    if jogador1_vitorias == 3:
        print(f"{jogador1} venceu a partida!")
    else:
        print("O computador venceu a partida!")


# Função para jogar contra outro jogador
def jogar_contra_jogador():
    jogador1_vitorias = 0
    jogador2_vitorias = 0
    
    jogador1_nome = input("Digite o nome do jogador 1: ")
    jogador2_nome = input("Digite o nome do jogador 2: ")
    
    while jogador1_vitorias < 3 and jogador2_vitorias < 3:
        jogador1 = input(f"{jogador1_nome}, digite sua jogada (pedra, papel ou tesoura): ")
        jogador2 = input(f"{jogador2_nome}, digite sua jogada (pedra, papel ou tesoura): ")

        while jogador1 != 'pedra' and jogador1 != 'papel' and jogador1 != 'tesoura':
            print("Entrada inválida! Por favor, digite uma jogada válida (pedra, papel ou tesoura).")
            jogador1 = input(f"{jogador1_nome}, digite sua jogada (pedra, papel ou tesoura): ")

        while jogador2 != 'pedra' and jogador2 != 'papel' and jogador2 != 'tesoura':
            print("Entrada inválida! Por favor, digite uma jogada válida (pedra, papel ou tesoura).")
            jogador2 = input(f"{jogador2_nome}, digite sua jogada (pedra, papel ou tesoura): ")

        vencedor = determinar_vencedor(jogador1, jogador2)
        
        if vencedor == 'jogador1':
            jogador1_vitorias += 1
            print(f"{jogador1_nome} venceu a rodada!")
        elif vencedor == 'jogador2':
            jogador2_vitorias += 1
            print(f"{jogador2_nome} venceu a rodada!")
        else:
            print("Empate!")
            
        print(f"Placar atual: {jogador1_nome} - {jogador1_vitorias} x {jogador2_vitorias} - {jogador2_nome}\n")
    
    if jogador1_vitorias == 3:
        print(f"{jogador1_nome} venceu a partida!")
    else:
        print(f"{jogador2_nome} venceu a partida!")



# Início do jogo
def main():
    print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")
    opcao = input("Escolha 1 para jogar contra o computador ou 2 para jogar contra outro jogador: ")

    if opcao != '1' and opcao != '2':
        print("Opção inválida. Tente novamente.\n"
              "Digite 1 para jogar contra o PC ou 2 Para jogar contra um amigo\n")
        main()

    if opcao == '1':
        jogar_contra_computador()
    elif opcao == '2':
        jogar_contra_jogador()

main()