import os
os.system ('cls')

maior_peso=0
menor_peso=10000

for i in range(5):
    peso = float(input("Insira seu peso: "))

    if peso>maior_peso:
        maior_peso = peso
    
    elif peso<menor_peso:
        menor_peso = peso

print(f"O maior peso inserido foi de: {maior_peso} kg")
print(f"O menor peso inserido foi de: {menor_peso} kg")