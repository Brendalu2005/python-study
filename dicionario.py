import os 
os.system ('cls')

#dados = { 'nome': 'pedro' , 'idade' : 25 }
#print(dados['nome'])
#print(dados['idade'])

#Para o usuário inserir os dados

estado = {}
brasil = []

for i in range (0, 3):
    estado['uf'] = str(input("insira uma unidade federativa: "))
    estado['sigla'] = str(input("insira a sigla da respectiva unidade federativa: "))
    brasil.append(estado.copy())
    
for e in brasil: 
#lista
    for k, v in e.items():
#dicionário
        print(f" o campo {k} tem valor {v}")

print(brasil)