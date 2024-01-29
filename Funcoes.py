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

def faz_jogada(tabuleiro,linha,coluna):
    
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    
    return tabuleiro

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



#### TESTE