# Run time error

n = int(input())
amigos = {}
for i in range(n):
    entrada = input().split()
    amigos[entrada[0]] = entrada[1:]

while True:
    try:
        entrada = input().split()
        if entrada[1] in amigos[entrada[0]]:
            print('Uhul! Seu amigo secreto vai adorar o/')
        else: print('Tente Novamente!')
    except EOFError:
        break