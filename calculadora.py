import os
os.system ('cls')

def fun_soma( n1, n2):
    soma = n1 + n2 
    return soma
#sempre retornar a operação na função

def fun_sub(n1, n2):
    subtracao = n1 - n2
    return subtracao

def fun_multi(n1, n2):
    multiplicacao = n1 * n2
    return multiplicacao

def fun_divi(n1, n2):
    if n1 != 0 or n2 !=0:
        if n1 > n2:
            return f"divisao = {n1/n2}"
        else:
            return f"divisao = {n2/n1}"
    else:
        print("Impossível dividir por 0")

while True:
    numero1 = int(input("Insira o primeiro número: "))
    numero2 = int(input("Insira o segundo número: "))
    print("Selecione uma operação:")
    print("\n1 - Soma \n2 - subtração \n3 - multiplicação \n4 - divisão")
    print("Caso queira encerrar digite '5'")
    codigo = int(input("Digite o código: "))

    if codigo == 1:
        resultado = fun_soma(numero1, numero2)
        print(resultado)

    elif codigo == 2:
        resultado = fun_sub(numero1, numero2)
        print(resultado)

    elif codigo == 3:
        resultado = fun_multi(numero1, numero2)
        print(resultado)
    
    elif codigo == 4:
        resultado = fun_divi(numero1, numero2)
        print(resultado)

    elif codigo == 5:
        break

    else:
        print ("Error")