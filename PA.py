import os 
os.system ('cls')

a1=int(input("insira o primeiro termo: "))
#Primeiro termo da PA

r=int(input("insira o valor da razão: "))
#Contagem da PA (2 em 2, 3 em 3 etc)

an = a1 + (10-1)*r
#Termo da PA que eu quero descobrir (na questão, está na 10 posição)
#quer os 10 primeiros números, ter certeza de que são contados 10 números

for n in range(a1, an+r, r):
    #termo inicial, termina no valor de an + a cobtagem, e o valor da contagem 
    print(f"{n}", end= ' --> ')

print("Fim")