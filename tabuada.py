import os
os.system ('cls')

numero = int(input("digite um número para sua tabuada: "))
print('-'*12)
for i in range (1, 11, 1):
    produto = i*numero
    print(f"{i} x {numero} = {produto}")
    
print('-'*12)