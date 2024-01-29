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

    # TODO: Implemente aqui a lógica para perguntar a linha que o jogador deseja atirar
    ataque_linha = input("Insira a linha que deseja atirar: ")
    if ataque_linha.isdigit(): 
        ataque_linha = int(ataque_linha)
        if ataque_linha < 0 or ataque_linha > 9:
            print('Linha inválida!')

        # TODO: Implemente aqui a lógica para perguntar a coluna que o jogador deseja atirar
        else:
            ataque_coluna = input("Insira a coluna que deseja atirar: ")
            if ataque_coluna.isdigit(): 
                ataque_coluna = int(ataque_coluna)
                if ataque_coluna < 0 or ataque_coluna > 9:
                    print('Coluna inválida!')

                # TODO: Implemente aqui a lógica para verificar se a linha e coluna não foram escolhidas anteriormente
                else:
                    if tabuleiro_oponente[ataque_linha][ataque_coluna] != 0 and tabuleiro_oponente[ataque_linha][ataque_coluna] != 1:
                        print(f'A posição linha {ataque_linha} e coluna {ataque_coluna} já foi informada anteriormente!')

                    else:
                        tabuleiro_oponente = faz_jogada(tabuleiro_oponente,ataque_linha,ataque_coluna)

                        # TODO: Implemente aqui a lógica para verificar se o jogador derrubou todos os navios do oponente
                        navios_afundados = afundados(frota_oponente,tabuleiro_oponente)
                        if navios_afundados == len(frota_oponente):
                            print('Parabéns! Você derrubou todos os navios do seu oponente!')
                            jogando = False

                        # TODO: Implemente aqui a lógica para que o oponente jogue caso ele ainda tenha navios                 
                        else:
                            while True:
                                ataque_linha_oponente = random.randint(0,9)
                                ataque_coluna_oponente = random.randint(0,9)
                                if tabuleiro_jogador[ataque_linha_oponente][ataque_coluna_oponente] == 0 or tabuleiro_jogador[ataque_linha_oponente][ataque_coluna_oponente] == 1:
                                    tabuleiro_jogador = faz_jogada(tabuleiro_jogador,ataque_linha_oponente,ataque_coluna_oponente)
                                    navios_afundados_oponente = afundados(frota_jogador,tabuleiro_jogador)
                                    print(f'Seu oponente está atacando na linha {ataque_linha_oponente} e coluna {ataque_coluna_oponente}')
                                    if navios_afundados_oponente == len(frota_jogador):
                                        print('Xi! O oponente derrubou toda a sua frota =(')
                                        jogando = False
                                    break
            else:
                print('Coluna inválida!')
    else:
        print('Linha inválida!')
