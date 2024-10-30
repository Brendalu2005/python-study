import os
os.system ('cls')

valores = [3, 4 , 5, 8, 9]

def dobro(num):
    posicao = 0
    while posicao < len(num):
        num[posicao] *= 2
        #para que o valor dessa posição receba o dobro de seu valor
        posicao += 1

valores = [3, 4 , 5, 8, 9]
dobro(valores) # chama a função para modificar valores
#a função dobro não retorna nenhum valor
print(valores) #imprime já modificada, não precisa chamar a lista novamente

