import os
os.system ('cls')

# Problema "alturas" 
# Fazer um programa para ler nome, idade e altura de N pessoas, conforme exemplo. Depois, mostrar na 
# tela a altura média das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos, 
# bem como os nomes dessas pessoas caso houver. 
# Exemplo: 
# Quantas pessoas serao digitadas? 5
# Dados da 1a pessoa: 
# Nome: Joao
# Idade: 15
# Altura: 1.82
# Dados da 2a pessoa: 
# Nome: Maria
# Idade: 16
# Altura: 1.60
# Dados da 3a pessoa: 
# Nome: Teresa
# Idade: 14
# Altura: 1.58
# Dados da 4a pessoa: 
# Nome: Carlos
# Idade: 21
# Altura: 1.65
# Dados da 5a pessoa: 
# Nome: Paulo
# Idade: 17
# Altura: 1.78
# Altura média: 1.69 
# Pessoas com menos de 16 anos: 40.0% 
# Joao 
# Teresa

nome_total = []
altura_total = []
idade_total= []
nome_menores = []
total_pessoas = 0 
cont_novo = 0



pessoas = int(input("Quantas pessoas serão digitadas? "))

for i in range (pessoas):
    nome=input("insira seu nome: ")
    nome_total.append(nome)
    idade=int(input("insira sua idade: "))
    idade_total.append(idade)
    altura=float(input("insira sua altura: "))
    altura_total.append(altura)
    total_pessoas+=1
    
    if idade < 16:
        cont_novo = cont_novo + 1
        nome_menores.append(nome)

altura_media = sum(altura_total) / total_pessoas
porcentagem = (cont_novo / total_pessoas)*100

print(f"A média das alturas é de: {altura_media:.2f} ")
print(f"o percentual dos usuários com menos de 16 anos é de: {porcentagem:.2f} ")

if cont_novo == 0:
    print("Não há usuários com menos de 16 anos")
else:
    print(nome_menores)


