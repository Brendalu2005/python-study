import os
os.system ('cls')

cont_homem=0
cont_mulher=0
idade_homem=0
idade_mulher=0
idade_menor=100

for i in range (5):
    genero=input("Insira seu genero: ")
    idade=int(input("Insira sua idade: "))
 
    if genero == "H" or genero=="h":
        cont_homem = cont_homem + 1
        idade_homem = idade_homem + idade

    elif genero == "M" or genero == "m":
        cont_mulher = cont_mulher + 1 
        idade_mulher = idade_mulher + idade

        if idade < idade_menor:
            idade_menor = idade
        
        

cont_total = cont_homem + cont_mulher
idade_total = idade_homem + idade_mulher
media = idade_total/cont_total

if cont_homem> 0:
    print(f"A quantidade de homens que participaram foi de: {cont_homem}")
else: 
    print("Não houveram homens cadastrados")
    
if cont_mulher > 0:
    print(f"A menor idade entre as mulheres foi de: {idade_menor}")
else:
    print("Não houveram mulheres cadastradas")

print(f"A média de todas as idades foi de: {media}")


    
    

    


