import os 
os.system ('cls')
cont_maior = 0
cont_menor = 0 

from datetime import date
atual=date.today().year
for i in range (7):
    ano = int(input("Insira o ano em que você nasceu: "))
    idade = atual - ano 
    print(f"Você tem {idade} anos")

    if idade>17:
        cont_maior = cont_maior + 1 

    else:
        cont_menor = cont_menor + 1

print(f"A quantidade de usuários que atigiram a maioridade é de: {cont_maior}")  
print(f"A quantidade de usuários que atigiram a menoridae é de: {cont_menor}")  

