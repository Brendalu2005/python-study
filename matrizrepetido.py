import os
os.system ('cls')

matriz = [[], [], [], []]
ocorrencias = []
#ocorrencias armazena todos os números únicos encontrados na matriz.
duplicados= []
#duplicados armazena apenas aqueles números que foram encontrados
# mais de uma vez, garantindo que não haja repetições.
#vai armazenar os números que se repetem

for l in range(4):
    for c in range(4):
        num = int(input(f"Insira um valor para [{l}][{c}]: "))
        matriz[l].append(num)

for l in range(4):
    for c in range(4): 
        print(f"[{matriz[l][c]}]", end = " ")
    print()

for l in matriz:
    for n in l:
        if n in ocorrencias:
            if n not in duplicados:
                duplicados.append(n)
        else:
            ocorrencias.append(n)
#Quando um número que já está em ocorrencia é encontrado, 
#o programa verifica se ele também está em duplicados.

#Se não estiver em duplicados, o número é adicionado,
#garantindo que cada número duplicado seja listado apenas uma vez.

if duplicados :
    print("Números duplicados: ")
    print(duplicados)
else:
    print("não existem números duplicados")