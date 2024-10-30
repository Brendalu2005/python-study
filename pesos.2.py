import os
os.system ('cls')

maior_peso=float('-inf')
#Qualquer número inserido será maior que maior_peso; menor valor possivel
menor_peso=float('inf')
#Qualquer numero inserido será menor que menor_peso; maior valor possivel

for i in range(5):
    peso = float(input("Insira seu peso: "))

    if peso>maior_peso:
        maior_peso = peso

    if peso<menor_peso:
         menor_peso = peso

print(f"O maior peso inserido foi de: {maior_peso} kg")
print(f"O menor peso inserido foi de: {menor_peso} kg")