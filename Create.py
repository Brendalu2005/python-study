import os
os.system ('cls')


lista = []


while True:
    print("1. CREATE")
    print("2. READ") 
    print("3. UPDATE")
    print("4. DELETE") 
    print("5. Encerrar o código.")
    #Colocar dentro do while pra se repetir no loop

    codigo = int(input("Digite um código: "))

    if codigo == 1:
        nome = input("insira um nome: " )
        lista.append(nome)
        continue

    elif codigo == 2:
        print(lista)
        continue

    elif codigo == 3:
        i = int(input("digite o índice para substituir: "))
        if 0<= i < len(lista):
    #i = equivale ao índice que será substituido
    #len(): mostra a quantidade de indices da lista
            novo_nome = input("Adicione o novo nome: ")
            lista[i] = novo_nome
    #insert NÃO substitui, apenas põe o nome novo no indice escolhido, mas não realiza substituição
        else: 
            print("índice inválido")
        continue

    elif codigo == 4:
        i2 = int("digite o indice que você quer remover: ")
        if 0<= i2 < len(lista):
            lista.pop(i2)
    #.pop() = remove o valor pelo índice
    #.remove = remove o indice pelo valor
        print(lista)
        continue



    elif codigo == 5:
       break

    else:
        print("Código inválido")