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