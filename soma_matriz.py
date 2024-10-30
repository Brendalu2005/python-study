import os
os.system ('cls')

matriz = [[],[]]
soma = 0 

for l in range(2):
    for c in range(2):
        num = int(input(f"Insira o valor para [{l}][{c}]: "))
#Colchetes apenas para fins estéticos ex: [0][0]
#chaves para formatação: mostra os indices das linhas e colunas para acrescentar o valor
        matriz[l].append(num)
#vai acrescentar os números nas linhas (linhas para colunas)
#primeiro são inseridas todas as linhas para formarem as colunas
#Não faz nada no primeiro for (só adicionar os valores ao índices da matriz)

for l in range(2):
        for c in range(2):
            soma += matriz[l][c]
            print(f"[{matriz[l][c]}]", end = " ")
        print()

print(f"A soma dos elementos é: {soma}")