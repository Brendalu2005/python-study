import os
os.system ('cls')

pares=0

for i in range (1,7):
    numero=int(input("digite um número: "))

    if numero%2==0:
        pares = pares + numero
    

print(f"a soma dos pares é de: {pares}")