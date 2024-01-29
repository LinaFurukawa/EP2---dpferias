import random
from Funcoes import *

# Gerando frota de forma aleatório para jogadores
frota_jogador = gerando_frota_automaticamente()
frota_oponente = gerando_frota_automaticamente()

# Criando tabuleiro com as frotas posicionadas
tabuleiro_jogador = posiciona_frota(frota_jogador)
tabuleiro_oponente = posiciona_frota(frota_oponente)
jogando = True
while jogando:

    # Imprimindo tabuleiro
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    coordenada_repetida = True
    while coordenada_repetida:

        # TODO: Implemente aqui a lógica para perguntar a linha que o jogador deseja atirar
        linha_invalida = True
        while linha_invalida:
            ataque_linha = input("Insira a linha que deseja atirar: ")
            if ataque_linha.isdigit(): 
                ataque_linha = int(ataque_linha)
                if ataque_linha < 0 or ataque_linha > 9:
                    print('Linha inválida!')
                else:
                    linha_invalida = False
            else:
                print('Linha inválida!')

        # TODO: Implemente aqui a lógica para perguntar a coluna que o jogador deseja atirar
        coluna_invalida = True
        while coluna_invalida:
            ataque_coluna = input("Insira a coluna que deseja atirar: ")
            if ataque_coluna.isdigit(): 
                ataque_coluna = int(ataque_coluna)
                if ataque_coluna < 0 or ataque_coluna > 9:
                    print('Coluna inválida!')
                else:
                    coluna_invalida = False
            else:
                    print('Coluna inválida!')

        # TODO: Implemente aqui a lógica para verificar se a linha e coluna não foram escolhidas anteriormente
        if tabuleiro_oponente[ataque_linha][ataque_coluna] != 0 and tabuleiro_oponente[ataque_linha][ataque_coluna] != 1:
            print(f'A posição linha {ataque_linha} e coluna {ataque_coluna} já foi informada anteriormente!')
        else:
            coordenada_repetida = False

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente,ataque_linha,ataque_coluna)

    # TODO: Implemente aqui a lógica para verificar se o jogador derrubou todos os navios do oponente
    navios_afundados = afundados(frota_oponente,tabuleiro_oponente)
    if navios_afundados == len(frota_oponente):
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
