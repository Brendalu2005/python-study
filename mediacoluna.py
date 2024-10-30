import os 
os.system ('cls')

matriz = [[], [], [], []]
soma = 0

for l in range(3):
    for c in range(4):
        num = int(input(f"insira os valores para [{l}] [{c}]: "))
        matriz[l].append(num)
#Aqui só adiciona na matriz


for l in range(3):
    for c in range(4):
        soma += matriz[l][c]

        print(f"[{matriz[l][c]:^2}]", end = " ")
    
    print()
#Aqui faz todo resto (operação, print etc)
media = soma/12

print(f"a média é: {media}")
