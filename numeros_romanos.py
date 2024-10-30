import os
os.system ('cls')

def numero_romano(n):
    if n < 1 or n > 999:
        return "Número fora do intervalo permitido (1 a 999)"
    
    # Mapeamento de números romanos
    numeros = [
        [1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], 
        [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], 
        [4, 'IV'], [1, 'I']
    ]
     # 18 é maior que 10 (subtrai, sobra 8), 8 não é maior que 9 então subtrai 
     # por 5 e assim por diante até chegar em 0
    resultado = ""
    #valor = numero
    #simbolo = numero romano
    for valor, simbolo in numeros:
    #Vai verificar cada valor e símbolo dentro da lista
        while n >= valor:
            n -= valor
            #n = n - valor
            resultado += simbolo
            #resultado = resultado + simbolo
    
    return resultado
            
#exemplo = 18
# 18 - 3 = 15 (III) subtrai por 1 tres vezes
# 15 - 5 = 10 (V)
#10 - 10 = 0 (X)
#Assim, subtraí o valor do numero inserido, pelo numero presente na lista até igualar a 0
#e assim, somar os simbolos
    
n = int(input("Insira um número: "))
resultado = numero_romano(n)
#chamar a função
print (resultado)
