import os
os.system ('cls')

A = []

for i in range (0, 100):
    numero = float(input("insira um número: "))
    A.append(numero)

for indice, valor in enumerate(A):
    if valor <= 10:
        print(f"A[{indice}] = {valor}")

        




