import os
os.system ('cls')

A = []

for i in range (0, 5):
    numero = float(input("insira um número: "))
    A.append(numero)

indice = 0
for valor in A:
    if valor <= 10:
        print(f"A[{indice}] = {valor}")

    indice+=1
        




