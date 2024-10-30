import os 
os.system ('cls')

dados = []
pessoas = [["Maria", 22], ["Heitor", 33]]
#Maria é o elemento 0, dentro da lista 0
#22 é o elemento 1, dentro da lista 0

dados.append("Pedro")
dados.append(25)

pessoas.append(dados[:])


print(dados)
print(pessoas)
for i in pessoas:
    print(i)
    print(f'O usuário {i[0]} tem {i[1]} anos')
#cada nome tem o índice 0, e cada idade tem índice 1, dentro de cada respectiva lista
print(pessoas[0][0])
print(pessoas[2][0])

