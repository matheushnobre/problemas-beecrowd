# Ainda não cheguei a solução correta

def ler_entrada():
    n1, n2 = input().split(' ')
    return int(n1), int(n2)

def contar_digitos(inicio, fim):
    sequencia = ''
    while inicio <= fim:
        sequencia += str(inicio) + ' '
        inicio += 1
        
    resposta = ''
    for i in range(10):
        resposta += str(sequencia.count(str(i))) + ' '
    
    return resposta

while True:
    n1, n2 = ler_entrada()
    
    if n1 == 0 and n2 == 0:
        break
    
    print(contar_digitos(n1, n2))