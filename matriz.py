import os
os.system ('cls') 

matriz = []

L = int(input("Insira a linha para realizar a operação: "))
#Linha que o usuário vai escolher para realizar a operação
print("Digite 'S' para soma e 'M' para média")
op = input("Qual operação você deseja realizar: ")

for l in range (2):
    linha = []
    for c in range (2):
        numero = int(input("Digite um número: "))
        linha.append(numero)
    matriz.append(linha)

if op == 'S':
    result = sum(matriz[L]) 

elif op == 'M':
    result = sum(matriz[L])/2

print(f"{result:.1f}")