# A solução está quase correta, não bate com o resultado da beecrowd por décimos

import math

def realizar_lancamento(altura_inicial, angulo, velocidade):
    gravidade = 9.80665 # valor da gravidade
    
    # calculando os cossenos e senos do ângulo de lançamento
    cosseno_angulo = round(math.cos(math.radians(angulo)), 5)
    seno_angulo = round(math.sin(math.radians(angulo)), 5)
    
    # calculando os componentes horizontal e vertical de velocidade
    vx = round(velocidade * cosseno_angulo, 5)
    vy = round(velocidade * seno_angulo, 5)
    
    tempo_subida = round(vy / gravidade, 5) # calculando tempo de subida
    altura_maxima = round(((vy**2) / (2*gravidade)) + altura_inicial, 5) # calculando a altura máxima
    tempo_descida = round(math.sqrt(2*altura_maxima / gravidade), 5) # calculando o tempo de descida
    tempo_total = round(tempo_subida + tempo_descida, 5) # calculando o tempo total
    
    alcance = round(vx * tempo_total, 5) # calculando o alcance
        
    return alcance

def acertou_nlogonia(p1, p2, alcance):
    return True if (alcance >= p1) & (alcance <= p2) else False
    
while True:
    try:
        altura = float(input()) # lê a altura inicial do lançamento
        p1, p2 = input().split(' ') # lê o ponto inicial e final da Nlogônia
        p1 = float(p1)
        p2 = float(p2)
        tentativas = int(input()) # lê o número de tentativa

        # verificando cada tentativa de lançamento
        for i in range(tentativas):
            angulo, velocidade = input().split(' ') # lê o ângulo e a velocidade do lançamento
            angulo = float(angulo)
            velocidade = float(velocidade)
            
            alcance = realizar_lancamento(altura, angulo, velocidade) # realizando o cálculo de alcance do lançamento
            
            # verificando se o lançamento atingiu Nlogonia e imprimindo resultado na tela
            if acertou_nlogonia(p1, p2, alcance):
                print("{} -> DUCK".format(alcance))
            else:
                print("{} -> NUCK".format(alcance))
                
    except EOFError:
        break