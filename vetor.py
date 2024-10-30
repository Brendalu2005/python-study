import os
os.system ('cls')

# Problema "negativos" 
# Faça um programa que leia um número inteiro positivo N (máximo = 10) e depois N números inteiros 
# e armazene-os em um vetor. Em seguida, mostrar na tela todos os números negativos lidos. 
# Exemplo: 
# Quantos numeros voce vai digitar? 6
# Digite um numero: 8
# Digite um numero: -2
# Digite um numero: 9
# Digite um numero: 10
# Digite um numero: -3
# Digite um numero: -7
# NUMEROS NEGATIVOS: 
# -2 
# -3 
# -7

N = []

limite = int(input("Quantos numeros você vai digitar?: "))

for i in range (limite):
    num = int(input("Digite um número: "))
    N.append(num)

print("NÚMEROS NEGATIVOS:")

for i in N:
    if i<0:
        print(i)
        
    

