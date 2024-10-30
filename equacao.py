import os
os.system ('cls')

num = int(input("Insira quantas equações você quer: "))

for i in range (num):
    a = int(input("digite um numero para 'a': "))
    b = int(input("digite um numero para 'b': "))
    c = int(input("digite um numero para 'c': "))

    if a == 0: 
        print("Não é uma função quadrática")

    else:
        delta = b**2 - 4 * a * c
        
        if delta == 0:
            raiz_1 = (- b + delta**0.5)/2*a
            print("Há uma raiz real")
            print(f"A raiz real equivale a:{raiz_1}")

        elif delta > 0:
            x1 = (- b + delta**0.5)/2*a
            x2 = (- b - delta**0.5)/2*a
            print("Há duas raizes reais")
            print(f"As raízes são: {x1} e {x2}")
        
        elif delta < 0:
            print("Não há raízes reais")
