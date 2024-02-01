while True: 
    id_teste = 1 # variável que armazena qual é o caso de teste
    
    # lendo um caso de teste
    teste = input().split(' ')
    n = int(teste[0]) # n -> número de mármores
    q = int(teste[1]) # q -> quantidade de consultas

    # verificando se é o caso de teste que encerra o programa
    if (n == 0) & (q == 0):
        break
    
    nums = [] # lista que armazenará os números
    # lendo os números escritos em cada mármore e armazenando-os na lista
    for i in range(n):
        nums.append(int(input()))
        
    print("CASE# {}:".format(id_teste))
    for i in range(q):
        consulta = int(input()) # lê qual número deve ser consultado
        if consulta not in nums:
            print("{} not found".format(consulta))
        else:
            posicao = nums.index(consulta) + 2
            print("{} found at {}".format(consulta, posicao))
        
    id_teste += 1