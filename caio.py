import os
os.system("cls")

matriza=[[] for i in range(3)]
matrizb=[[] for j in range(3)]

for l in range(3):
    for c in range(3):
        n=int(input(f"Digite um valor para matriza [{l+1},{c+1}]: "))
        matriza[l].append(n)

for l in range(3):
    for c in range(3):
        n1=int(input(f"Digite um valor para  [{l+1},{c+1}]: "))
        matrizb[l].append(n1)

resultado=[[] for k in range(3)]
for l in range(3):
    for c in range(3):
        for k in range(3):
            resultado[l][c]+= matriza[l][k] * matrizb[l][k]

for l in range(3):
    for c in range(3):
        print(resultado[l][c],end=" ")
    print