import os
os.system ('cls')

def vitamina_c(num):
    alimentos = [
    ["suco de laranja", 120], ["morango fresco", 85],
    ["mamao", 85], ["goiaba vermelha", 70], ["manga", 56],
    ["laranja", 50], ["brocolis", 34]
      
    ]
    while True:
        t = int(input("insira a quantidade de alimentos"))
        if t == 0:
            break

        elif t<1 or t>7:
            print("error")
        
        else:
            for i in range (t):
                comida = input().split().strip() 
                #adiciona as comidas inseridas numa lista e remove espaçamentos
                

            

 = str(input())
t = int(input())