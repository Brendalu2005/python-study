import os
os.system ('cls')

n=int(input("insira um número: "))

for i in range (2, n + 1):
    #i é um número entre 2 e n + 1
    #contando de 2 até o número que o usuário inserir
    #não pode contar apartir de um, pois todo número é multiplo de 1 e dele mesmo
    primos = True

    for j in range (2, i):
        #j é um número entre 2 e o dentro do intervalo do número inserido pelo usuário
        if i % j == 0:
            #não pode ser j % i, se não a condição sempre estará errada e todos serão primos
            primos = False
    
    if primos:
        print(f"{i} é um número primo")
    
    else:
        print(f"{i} não é um número primo")


