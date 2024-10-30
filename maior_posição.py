import os
os.system ('cls')

# Problema "maior_posicao" 
# Faça um programa que leia N números reais e armazene-os em um vetor. Em seguida, mostrar na tela 
# o maior número do vetor (supor não haver empates). Mostrar também a posição do maior elemento, 
# considerando a primeira posição como 0 (zero). 
# Exemplo: 
# Quanto numeros voce vai digitar? 6
# Digite um numero: 8.0
# Digite um numero: 4.0
# Digite um numero: 10.0
# Digite um numero: 14.0
# Digite um numero: 13.0
# Digite um numero: 7.0
# MAIOR VALOR = 14.0 
# POSICAO DO MAIOR VALOR = 3

limite = int(input("Quantos números você vai digitar?: "))

Numeros_reais = []

for i in range(limite):
    num = float(input("Digite um número: "))
    Numeros_reais.append(num)

print(f"MAIOR VALOR = {max(Numeros_reais)}")
print(f"POSIÇÃO DO MAIOR VALOR = {Numeros_reais.index(max(Numeros_reais))}")


