import os
os.system('cls')
lista = []
for i in range(8):
    num = int(input("digite um número: "))
    lista.append(num)

lista_crescente = sorted(lista)
lista_decrescente = sorted(lista,reverse=True)
print(f"O máximo é: {max(lista)}, e o mínimo é: {min(lista)}")
print(f"A soma de todos os números é de: {sum(lista)}")
print(f"A lista em ordem crescente é: {lista_crescente}")
print(f"A lista em ordem decrescente é: {lista_decrescente}")

