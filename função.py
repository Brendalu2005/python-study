import os
os.system ('cls')

def media_valores (valor1, valor2):
    media = (valor1+valor2)/2
    return media

def status(media):
    if media >= 7:
        return("Aprovado")
    else:
        return("Reprovado")

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

resultado = media_valores(nota1, nota2)

print(resultado)
