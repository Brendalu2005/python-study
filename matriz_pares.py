import os
os.system ('cls')

matriz = [[], [], [], []]
pares = []
cont_par = 0

for l in range(4):
    for c in range(4):
        num = int(input(f"insira o valor para [{l}][{c}]: "))
        matriz[l].append(num)

for l in range(4):
    for c in range(4):
        print(f"[{matriz[l][c]:^1}]", end = " ")
    print()


for l in matriz:
    for n in l:
        if n % 2 == 0:
            cont_par += 1
            pares.append(n)
#l = linhas dentro da matriz
#n = valor dentro das linhas

   
if cont_par != 0 :
     print(f"Existem {cont_par} números pares na matriz")
     print(f"Os números pares são: {pares}")    
else:
     print("Não existem números pares")
        