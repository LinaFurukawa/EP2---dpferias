import random

# PARA TESTAR O SEU CÓDIGO NA ACADEMIA PYTHON SERÁ NECESSÁRIO COLAR AS FUNÇÕES DESENVOLVIDAS AQUI!!!

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    '''
    tabuleiro_jogador: tabuleiro do jogador
    tabuleiro_oponente: tabuleiro do oponente
    Função monta uma string com a representação dos tabuleiros do jogador e do oponente.
    O tabuleiro do jogador é representado por um tabuleiro com as posições dos navios.
    O tabuleiro do oponente é representado por um tabuleiro com as posições que o jogador já atirou.
    '''

    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item)
                                  for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join(
            [info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    texto += '_______________________________      _______________________________\n'
    return texto


def gerando_frota_automaticamente():
    '''
    Função gera uma frota de navios de forma aleatória.
    '''
    quantidades = {
        "submarino": {
            "quantidade": 4,
            "tamanho": 1
        },
        "destroyer": {
            "quantidade": 3,
            "tamanho": 2
        },
        "navio-tanque": {
            "quantidade": 2,
            "tamanho": 3
        },
        "porta-aviões": {
            "quantidade": 1,
            "tamanho": 4
        }
    }

    frota = []

    for nome_navio, info in quantidades.items():
        for _ in range(info["quantidade"]):
            dados_de_posicionamento = {
                "tamanho": info["tamanho"],
            }
            dados_de_posicionamento["orientacao"] = random.choice(
                ["vertical", "horizontal"])
            dados_de_posicionamento["linha"] = random.randint(0, 9)
            dados_de_posicionamento["coluna"] = random.randint(0, 9)

            while not posicao_valida(dados_de_posicionamento, frota):
                dados_de_posicionamento["orientacao"] = random.choice(
                    ["vertical", "horizontal"])
                dados_de_posicionamento["linha"] = random.randint(0, 9)
                dados_de_posicionamento["coluna"] = random.randint(0, 9)

            preenche_frota(dados_de_posicionamento, nome_navio, frota)

    return frota

def preenche_frota(dados_posicion,tipo_navio,frota):

    linha = dados_posicion['linha']
    coluna = dados_posicion['coluna']
    orientacao = dados_posicion['orientacao']
    tamanho = dados_posicion['tamanho']

    novo_barco = {}
    novo_barco['tipo'] = tipo_navio
    novo_barco['posicoes'] = [[linha,coluna]]

    for i in range(tamanho-1):

        if orientacao == "horizontal":
            coluna += 1
        if orientacao == "vertical":
            linha += 1
        
        novo_barco['posicoes'].append([linha,coluna])

    frota.append(novo_barco)

    return frota

def posiciona_frota(frota):

    tabuleiro = []

    for linha in range(10):
        tabuleiro.append([])
        for coluna in range(10):
            tabuleiro[linha].append(0)

    for navio in frota:
        for posicoes in navio['posicoes']:
            linha_navio = posicoes[0]
            coluna_navio = posicoes[1]

            tabuleiro[linha_navio][coluna_navio] = 1

    return tabuleiro

def define_posicoes(dados_posicao):

    linha = dados_posicao["linha"]
    coluna = dados_posicao["coluna"]
    posicao = [[linha,coluna]]
    
    for i in range(dados_posicao["tamanho"]-1):

        if dados_posicao["orientacao"] == "vertical":
            linha += 1
        if dados_posicao["orientacao"] == "horizontal":
            coluna += 1

        posicao.append([linha,coluna])

    return posicao

def posicao_valida(dados_posicao,frota):

    novo_navio = define_posicoes(dados_posicao)

    for posicao_novo_navio in novo_navio:

        linha_novo_navio = posicao_novo_navio[0]
        coluna_novo_navio = posicao_novo_navio[1]
        if linha_novo_navio > 9 or coluna_novo_navio > 9:
            return False

        for navio in frota:
            for posicao in navio['posicoes']:
                if posicao == posicao_novo_navio:
                    return False
    
    return True

def faz_jogada(tabuleiro,linha,coluna):
    
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    
    return tabuleiro

def afundados(frota,tabuleiro):

    afundados = 0
    for navio in frota:

        acertos = 0
        for posicao in navio['posicoes']:
            linha_navio = posicao[0]
            coluna_navio = posicao[1]

            if tabuleiro[linha_navio][coluna_navio] == 'X':
                acertos += 1

        if acertos == len(navio['posicoes']):
            afundados += 1

    return afundados

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
