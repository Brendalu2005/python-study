import os
os.system ('cls')

frutas_lista = {}


while True:
    print("digite 'sair' em frutas para encerrar")
    frutas = input("digite a fruta: ").lower()
    if frutas == 'sair':
        break
    quantia = int(input("digite a quantidade de frutas em estoque: "))

    frutas_lista[frutas] = [quantia]

if ("maçã" in frutas_lista) == False:
    print("Não existem maçãs no estoque")
else:
    print(f"A quantidade de maçãs é de: {str(frutas_lista["maçã"])}")

if frutas_lista.get("banana"):
    print("Existem bananas no estoque")
else:
    print("Não exitem bananas no estoque")

if ("laranja" in frutas_lista) == True:
    frutas_lista["laranja"] = [15]
else:
    print("Não há laranjas no estoque")

print(frutas_lista.pop("pera", "A pera não foi encontrada"))

print('-'*12)
print("lista de frutas e suas quantidades: ")

for frutas, quantia in frutas_lista.items():
    print(frutas,":", quantia)

print('-'*12)
