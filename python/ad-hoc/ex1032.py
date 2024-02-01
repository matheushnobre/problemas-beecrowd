# Timelimit

def is_prime(number):
    if number <= 1:
        return False
    else:
        for i in range(2, int(number/2+1)):
            if number % i == 0:
                return False
    return True

def proximo_primo(num):
    n = num+1
    while True:
        if is_prime(n):
            return n
        n += 1

def iniciar_posicoes(entrada):
    posicoes = []
    for i in range(entrada):
        posicoes.append(i+1)
    return posicoes

def jogar(entrada):
    posicoes = iniciar_posicoes(entrada)
    primo = 2
    executado = 1
    
    while (len(posicoes) != 1):
        executado = (executado-1 + primo) % len(posicoes)
        if executado == 0:
            executado = len(posicoes)
        posicoes.pop(executado - 1)
        primo = proximo_primo(primo)
        
    return posicoes[0]
        
while True:
    entrada = int(input())
    
    if entrada == 0:
        break
    
    print(jogar(entrada))