import os
os.system ('cls')

numeros_perfeitos = []

numero = int(input("digite um número: "))

for i in range(1, numero):
# vai percorrer todos os valores ate o número inserido
    if numero % i == 0:
#se um número dividido por seus antecessores é = 0, ele é perfeito
        numeros_perfeitos.append(i)

if sum(numeros_perfeitos)==numero:
    print(f"é um número perfeito")
else:
    print("Err0")
