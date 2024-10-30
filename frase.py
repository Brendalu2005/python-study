import os
os.system ('cls')

def cont_palavras(frase):
    palavras = frase.split()
    return len(palavras)
#obs: len() mostra a quantidade de objetos dentro de uma lista.
#.split() coloca todas as palavras de uma string dentro de uma lista, sem contar com os espaçamentos.
#divide as palavras.
#Def realiza a operação.

frase = str(input("Digite uma frase: "))
resultado = cont_palavras(frase)
#vai imprimir o resultado com as operações já realizadas.

print(resultado)
#ou print(cont_palavras(frase))
