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

