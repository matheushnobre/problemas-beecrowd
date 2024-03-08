# Wrong answer

t = int(input())

# Lendo cada caso de teste
for i in range(t):
    reprovados=''
    n = int(input()) # 1º linha (número de estudantes)
    estudantes = input().split() # 2º linha (nome dos estudantes)
    frequencias = input().split() # 3ª linha
    
    # Analisando a frequência de cada estudante
    for index, estudante in enumerate(estudantes):
        f = frequencias[index]
        aulas = len(f) - f.count('M')
        if 100/aulas * f.count('P') < 75: 
            reprovados += estudantes[frequencias.index(f)]+' '
    print(reprovados)