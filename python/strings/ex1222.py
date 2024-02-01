# Solução não bateu com o da Beecrowd

while True:
    try:
        # numero de palavras do conto, numero maximo de linhas por paginna, numero maximo de caracteres em uma linha 
        palavras_conto, max_linhas_pg, max_caracteres_linha = input().split(' ')
        palavras_conto = int(palavras_conto)
        max_linhas_pg = int(max_linhas_pg)
        max_caracteres_linha = int(max_caracteres_linha)

        # conto de Machado
        conto = input()

        num_paginas = 1
        num_caracteres_linha = 0
        num_linhas_pg = 1

        palavras = []
        for palavra in conto.split(' '):
            palavras.append(palavra)
            palavras.append(' ')
        palavras.pop()

        for palavra in palavras:
            num_caracteres_linha += len(palavra)
            if num_caracteres_linha > max_caracteres_linha:
                num_linhas_pg += 1
                num_caracteres_linha = len(palavra)
                if num_linhas_pg > max_linhas_pg:
                    num_paginas += 1
                    num_linhas_pg = 1

        print(num_paginas)
    except:
        break