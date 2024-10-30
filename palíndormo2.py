import os 
os.system ('cls')

#palindromo: palavra que é a mesma quando lida de trás para frente

frase= str(input("digite uma frase: ")).lower().replace(" ", "")

if frase == frase[::-1]:
    print(frase)
    print("é um palíndromo")

else:
    print("não é um palíndromo")


