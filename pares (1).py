import os
os.system ('cls')

pares = []

Qnt = int(input("Insira quantos números você vai digitar: "))

for i in range(Qnt):
    numero = int(input("Insira um número: "))

    if numero % 2 == 0:
        pares.append(numero)

print("NÚMEROS PARES:")
print(pares)
print("A quantidade")
