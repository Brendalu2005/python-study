import os
os.system ('cls')

numeros = []

N = int(input("Quantos números você quer digitar?: "))

for i in range(N):
    num = int(input("Insira um número: "))
    numeros.append(num)

print(numeros)
print(f"A soma da lista é de: {sum(numeros)}")
print(f"A média da lista é de: {sum(numeros)/N}")

